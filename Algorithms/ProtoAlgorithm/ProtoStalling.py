from typing import Dict, List, Tuple, Any, Set

from DataObjects.ClassState import State
from DataObjects.ClassStateSet import StateSet
from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassTransition import Transition

from Algorithms.General.Tracing.TraceTree import Trace

from Algorithms.ProtoAlgorithm.ProtoBase import ProtoBase


class ProtoStalling(ProtoBase):

    def __init__(self):
        ProtoBase.__init__(self)
        pass

    def concurrent_start_state_set_states(self,
                                          arch: Architecture,
                                          state_set: StateSet,
                                          start_state_set_to_remote_trace_list_map: Dict[StateSet, List[Trace]]) -> \
            bool:

        # Get new access traces, access traces change every iteration because new remote traces are inherited
        access_traces, _ = self.classify_traces_start_state(arch, state_set)

        remote_traces = start_state_set_to_remote_trace_list_map[state_set]

        new_states = False

        start_state_set = state_set.getstartstates()
        # The start state set list is permanently growing in the upper loop, thats why we need to know the maximum
        # index of the old elements
        max_start_state_set_index = len(start_state_set)

        for state_ind in range(0, max_start_state_set_index):
            state = start_state_set[state_ind]

            # Filter the traces that have not been inherited yet
            filtered_remote_traces = state.filter_remote_traces(remote_traces)
            state.add_inherited_traces(filtered_remote_traces)
            if filtered_remote_traces:
                new_states = True
            # Copy the traces
            new_remote_transition_sequences = self.generate_remote_transition_sequences(state, filtered_remote_traces)

            # Filter traces
            for new_remote_transition_sequence in new_remote_transition_sequences:

                if new_remote_transition_sequence[0].startState == new_remote_transition_sequence[-1].finalState:
                    continue

                # extract start_state guards
                guards_traces_dict = self.find_access_trace_guards(state, access_traces)

                for guard in guards_traces_dict:
                    guard_access_traces = guards_traces_dict[guard]

                    # Copy trace and update state names
                    final_sets = new_remote_transition_sequence[-1].finalState.getstatesets()

                    # Find new final state
                    finalstate = self._SetGuardSearch(guard, final_sets)

                    if finalstate:
                        new_remote_transition_sequence[-1].finalState = finalstate
                    else:
                        # Find current access traces that contain the state, there can exist more than one
                        filtered_access_traces = self.find_access_traces_by_state(state, guard_access_traces)

                        for access_trace in filtered_access_traces:
                            remain_access_trans = self.find_remaining_responses_(state, access_trace)
                            new_remote_transition_sequence[-1].finalState = remain_access_trans[0].startState

        return new_states

    def generate_remote_transition_sequences(self, start_state: State, remote_traces: List[Trace])\
            -> List[List[Transition]]:
        transition_sequences: List[List[Transition]] = []

        old_state_to_new_state_map: Dict[str, State] = {}
        old_trans_to_new_trans_map: Dict[int, Transition] = {}

        start_state_set_guards = self.extrace_guard_set_from_state_sets(start_state.startstateSets)
        end_state_set_guards = self.extrace_guard_set_from_state_sets(start_state.endstateSets)

        forbidden_guards: List[str] = list(start_state_set_guards.intersection(end_state_set_guards))

        for remote_trace in remote_traces:
            if [inmsg for inmsg in remote_trace.inmsg if str(inmsg) in forbidden_guards]:
                continue

            transition_sequences.append(self.copy_trace_or_trans_list_rename_states(start_state,
                                                                                    remote_trace,
                                                                                    old_trans_to_new_trans_map,
                                                                                    old_state_to_new_state_map,
                                                                                    forbidden_guards))
        return transition_sequences

    # Don't use SSP traces from level, because a new state might have been created in the meantime that satisfies the
    # trace conditions already
    def find_access_trace_guards(self, state: State, access_traces: List[Trace])\
            -> Dict[Tuple[Any, ...], List[Trace]]:
        # Create all traces from current stable state
        guard_tuples = {}
        for access_trace in access_traces:
            cur_guards = []
            for ind in range(0, len(access_trace.transitions)):
                cur_guards.append(access_trace.transitions[ind].getguard())
                if access_trace.transitions[ind].finalState == state:
                    guard_tuple = tuple(cur_guards)
                    if guard_tuple in guard_tuples:
                        guard_tuples[tuple(cur_guards)].append(access_trace)
                    else:
                        guard_tuples[tuple(cur_guards)] = [access_trace]
        return guard_tuples
