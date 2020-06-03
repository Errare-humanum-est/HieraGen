import copy

from typing import Dict, List, Tuple, Union

from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassStateSet import StateSet
from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition

from Algorithms.General.Tracing.TraceTree import Trace

from Algorithms.General.AuxStateHandler import AuxStateHandler
from Algorithms.General.GenDeferMessage import GenDeferMessage

from Algorithms.ProtoAlgorithm.ProtoBase import ProtoBase

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens


class ProtoNonStalling(ProtoBase):

    def __init__(self):
        ProtoBase.__init__(self)
        pass

    def concurrent_end_state_set_states(self,
                                        arch: Architecture,
                                        state_set: StateSet,
                                        start_state_set_to_remote_trace_list_map: Dict[StateSet, List[Trace]]) -> \
            bool:
        # Get new access traces, access traces change every iteration because new remote traces are inherited
        access_traces, _ = self.classify_traces_end_state(arch, state_set)

        remote_traces = start_state_set_to_remote_trace_list_map[state_set]

        new_states = False

        end_stable_state = state_set.getstablestate()
        end_state_set = state_set.getendstates()
        # The start state set list is permanently growing in the upper loop, thats why we need to know the maximum
        # index of the old elements
        max_end_state_set_index = len(end_state_set)

        for state_ind in range(0, max_end_state_set_index):
            state = end_state_set[state_ind]

            # No states that have a start state set must be covered
            if state.startstateSets or (state == end_stable_state):
                continue

            # Filter the traces that have not been inherited yet
            filtered_remote_traces = state.filter_remote_traces(remote_traces)
            state.add_inherited_traces(filtered_remote_traces)
            if filtered_remote_traces:
                new_states = True

            # Find current access traces that contain the state, there can exist more than one
            filtered_access_traces = self.find_access_traces_by_state(state, access_traces)
            filtered_remaining_trans_sequences = self.remaining_tranisition_list(state, filtered_access_traces)
            if not filtered_remaining_trans_sequences:
                continue

            # Copy the remote trigger transitions
            remote_trans_list = []
            for remote_trace in filtered_remote_traces:
                remote_trans = remote_trace.transitions[0]
                if remote_trans not in remote_trans_list:
                    remote_trans_list.append(remote_trans)

            # Filter traces
            for remote_trans in remote_trans_list:

                start_state_set_guards = self.extrace_guard_set_from_state_sets(state.endstateSets)
                end_state_set_guards = self.extrace_guard_set_from_state_sets(remote_trans.finalState.endstateSets)

                forbidden_guards: List[str] = list(start_state_set_guards.intersection(end_state_set_guards))

                if str(remote_trans.inMsg) in forbidden_guards:
                    continue

                # Remote trace assign new final state
                new_state_str = str(state) + "_" + \
                                str(remote_trans.startState) + "_" + \
                                remote_trans.getguard()
                new_state = State(new_state_str, self.access, self.evict)

                for endset in remote_trans.getfinalstate().getstatesets():
                    endset.addendstate(new_state)

                new_remote_trans = self._CopyModifyTransition(remote_trans, state, new_state)
                state.addtransitions(new_remote_trans)

                for trans in state.setTrans:
                    if trans.startState == trans.finalState:
                        copy_loop_trans = self._CopyModifyTransition(trans, new_state, new_state)
                        new_state.addtransitions(copy_loop_trans)

                defer_final_state = remote_trans.finalState

                # Copy the transitions required to complete the requests
                new_access_transition_sequences = self.copy_filtered_access_traces(new_state,
                                                                                   None,
                                                                                   filtered_remaining_trans_sequences,
                                                                                   forbidden_guards)

                # In transition push defer inmsg
                original_operation = copy.deepcopy(new_remote_trans.operation)
                defer_push_operation = GenDeferMessage().defer_push_message(new_remote_trans,
                                                                            MurphiTokens.tPUSH_STALL_DEFER)

                defer_pop_operation = GenDeferMessage().defer_pop_message(new_remote_trans,
                                                                          MurphiTokens.tPOP_STALL_DEFER)

                new_remote_trans.operation = [defer_push_operation]
                defer_pop_operation = [defer_pop_operation] + original_operation
                # Rename the variables
                AuxStateHandler.cond_operations_var_rename(defer_pop_operation,
                                                           str(new_remote_trans.inMsg),
                                                           MurphiTokens.vdeferpref + str(new_remote_trans.inMsg))

                push_trans_outmsg = new_remote_trans.outMsg
                new_remote_trans.outMsg = []

                for new_access_transition_sequence in new_access_transition_sequences:
                    defer_transition_sequence = [new_remote_trans] + new_access_transition_sequence
                    final_transition = defer_transition_sequence[-1]
                    final_transition.outMsg = copy.copy(final_transition.outMsg) + push_trans_outmsg

                    new_access_transition_sequence[-1].operation = \
                        copy.deepcopy(new_access_transition_sequence[-1].operation)
                    new_access_transition_sequence[-1].operation += defer_pop_operation

                    final_transition.finalState = defer_final_state

        return new_states

    @staticmethod
    def classify_traces_end_state(arch: Architecture,
                                  stateset: StateSet) -> Tuple[List[Trace], List[Trace]]:

        remote_traces = []
        access_traces = []

        # Classification can either be performed by analyzing initial classification of transition or
        # by simply checking whether trace has access field set...
        for trace in arch.traces.final_state_dict[stateset.getstablestate()]:
            if not trace.access:
                remote_traces.append(trace)
            else:
                access_traces.append(trace)

        return access_traces, remote_traces

    def remaining_tranisition_list(self, start_state: State, access_traces: List[Trace]) -> List[List[Transition]]:
        remain_transition_sequences: List[List[Transition]] = []

        for access_trace in access_traces:
            remain_transition_sequences.append(self.find_remaining_responses_(start_state, access_trace))
        return remain_transition_sequences

    def copy_filtered_access_traces(self,
                                    start_state: State,
                                    initial_transition: Transition,
                                    access_trans_sequence_list: List[List[Transition]],
                                    forbidden_guards: List[str]) \
            -> List[List[Transition]]:
        transition_sequences: Dict[Tuple[int, ...], List[Transition]] = {}

        old_state_to_new_state_map: Dict[str, State] = {}
        old_trans_to_new_trans_map: Dict[int, Transition] = {}

        for access_trans_sequence in access_trans_sequence_list:
            if not access_trans_sequence:
                continue

            if initial_transition:
                access_trans = [initial_transition] + access_trans_sequence
            else:
                access_trans = access_trans_sequence

            cur_access_sequence = self.copy_trace_or_trans_list_rename_states(start_state,
                                                                              access_trans,
                                                                              old_trans_to_new_trans_map,
                                                                              old_state_to_new_state_map,
                                                                              forbidden_guards)

            sequence_id = tuple([trans.get_hash() for trans in cur_access_sequence])
            transition_sequences[sequence_id] = cur_access_sequence

        return list(transition_sequences.values())
