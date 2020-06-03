import copy

from typing import Dict, List, Tuple, Union, Set

from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassStateSet import StateSet
from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition
from Algorithms.General.Tracing.TraceTree import Trace

from Monitor.ProtoCCTable import *

class ProtoBase:

    def __init__(self):
        self.access = None  # Shadowed by ProtoAlgorithm variables
        self.evict = None   # Shadowed by ProtoAlgorithm variables

    @staticmethod
    def extrace_guard_set_from_state_sets(state_sets: List[StateSet]) -> Set[str]:
        guards = []
        for state_set in state_sets:
            for trans in state_set.getstablestate().setTrans:
                guards.append(trans.getguard())
        return set(guards)


    @staticmethod
    def classify_traces_start_state(arch: Architecture,
                                    stateset: StateSet) -> Tuple[List[Trace], List[Trace]]:

        remote_traces = []
        access_traces = []

        # Classification can either be performed by analyzing initial classification of transition or
        # by simply checking whether trace has access field set...
        for trace in arch.traces.start_state_dict[stateset.getstablestate()]:
            if not trace.access:
                remote_traces.append(trace)
            else:
                access_traces.append(trace)

        return access_traces, remote_traces

    def find_access_traces_by_state(self, start_state: State, access_traces: List[Trace]):
        found_traces = []
        for access_trace in access_traces:
            if start_state in access_trace.states:
                found_traces.append(access_trace)
        return found_traces

    def find_remaining_responses_(self, state: State, access_trace: Trace) -> List[Transition]:
        for ind in range(0, len(access_trace.transitions)):
            if state == access_trace.transitions[ind].startState:
                return access_trace.transitions[ind:]

    @staticmethod
    def _CopyModifyTransition(transition: Transition, startstate: State, finalstate: State):
        newtrans = copy.copy(transition)
        newtrans.setstartstate(startstate)
        newtrans.setfinalstate(finalstate)
        return newtrans

    def _SetGuardSearch(self, guards, finalsets) -> Union[State, None]:
        for finalset in finalsets:
            state = finalset.getstablestate()
            found = 0
            ind = 0

            if guards != 0:
                while ind < len(guards):
                    transition = state.gettransitionbyguard(guards[ind])

                    if isinstance(transition, list):
                        ProtoCCTablePrinter.ptransitions(transition)
                        assert 0, "No support yet for transition list"

                    if transition:
                        state = transition.getfinalstate()
                        if ind == len(guards) - 1:
                            found = 1
                        ind += 1
                    else:
                        ind = len(guards)

            if found:
                if set(state.getstatesets()).issuperset(set(finalsets)):
                    return state
            else:
                return None
        return None

    def copy_trace_or_trans_list_rename_states(self,
                                               start_state: State,
                                               remote_trace: Union[Trace, List[Transition]],
                                               old_trans_to_new_trans_map: Dict[int, Transition],
                                               old_state_to_new_state_map: Dict[str, State],
                                               forbidden_guards: List[str]) \
            -> List[Transition]:

        remote_transitions = remote_trace
        if isinstance(remote_trace, Trace):
            remote_transitions = remote_trace.transitions

        remote_trace_trans_mod = []
        moving_start_state = start_state

        for ind in range(0, len(remote_transitions)):
            cur_transition = remote_transitions[ind]

            # Check if the current transition has been copied before
            cur_trans_hash = cur_transition.get_hash()
            if cur_trans_hash in old_trans_to_new_trans_map:
                remote_trace_trans_mod.append(old_trans_to_new_trans_map[cur_trans_hash])
                moving_start_state = old_trans_to_new_trans_map[cur_trans_hash].finalState
            else:
                if cur_transition.startState == cur_transition.finalState:
                    new_trans = self._CopyModifyTransition(cur_transition, moving_start_state, moving_start_state)
                    start_state.addtransitions(new_trans)
                else:
                    final_state = None
                    if ind == len(remote_transitions)-1:
                        final_state = cur_transition.finalState

                    moving_start_state, new_trans = self.copy_modify_state(moving_start_state,
                                                                           remote_transitions[ind],
                                                                           old_state_to_new_state_map,
                                                                           forbidden_guards,
                                                                           final_state
                                                                           )

                remote_trace_trans_mod.append(new_trans)
                old_trans_to_new_trans_map[cur_trans_hash] = new_trans

        if remote_transitions[0].startState == remote_transitions[-1].finalState:
            remote_trace_trans_mod[-1].finalState = start_state

        remote_trace_trans_mod[0].startState = start_state

        return remote_trace_trans_mod

    # Transition is first of remote_trans
    def copy_modify_state(self, startstate: State,
                          transition: Transition,
                          old_state_to_new_state_map: Dict[str, State],
                          forbidden_guards: List[str],
                          final_state: [State, None] = None):
        # If a known final state exists, then
        if final_state:
            newstate = final_state
            if str(final_state) in old_state_to_new_state_map:
                newstate = old_state_to_new_state_map[str(final_state)]
        else:
            new_state_str = startstate.getstatename() + "_" + transition.getguard()
            if new_state_str in old_state_to_new_state_map:
                newstate = old_state_to_new_state_map[new_state_str]
            else:
                newstate = State(new_state_str, self.access, self.evict)
                old_state_to_new_state_map[new_state_str] = newstate

                # The new_state replaces the final state so it must possess all local access permissions
                for trans in transition.startState.setTrans:
                    if str(trans.inMsg) in forbidden_guards:
                        continue

                    if trans.startState == trans.finalState:
                        new_trans = self._CopyModifyTransition(trans, newstate, newstate)
                        newstate.addtransitions(new_trans)

                for trans in transition.finalState.setTrans:
                    if str(trans.inMsg) in forbidden_guards:
                        continue

                    if trans.startState == trans.finalState:
                        new_trans = self._CopyModifyTransition(trans, newstate, newstate)
                        newstate.addtransitions(new_trans)

                # The new_state replaces the final state so it must possess all local access permissions
                for trans in startstate.setTrans:
                    if str(trans.inMsg) in forbidden_guards:
                        continue

                    if trans.startState == trans.finalState:
                        new_trans = self._CopyModifyTransition(trans, newstate, newstate)
                        newstate.addtransitions(new_trans)

                for startset in transition.getfinalstate().getstatesets():
                    startset.addstartstate(newstate)

                for endset in startstate.getendstatesets():
                    endset.addendstate(newstate)

        # Create vertice
        new_trans = self._CopyModifyTransition(transition, startstate, newstate)
        startstate.addtransitions(new_trans)

        return newstate, new_trans
