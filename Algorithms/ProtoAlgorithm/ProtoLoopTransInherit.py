from Algorithms.General.Tracing.TraceTree import create_trace_tree
from Algorithms.General.GenStateSets import extract_states_from_sets

from Algorithms.General.GenStateSets import get_stable_states
from Algorithms.ProtoAlgorithm.ProtoBase import ProtoBase
from Algorithms.General.GenStateSets import StateSets

from DataObjects.ClassStateSet import StateSet


class ProtoLoopTransInherit(ProtoBase):

    def __init__(self):
        ProtoBase.__init__(self)
        pass

    def _Loop_Trans_Inheritance(self, state_sets: StateSets):
        for state_set in state_sets:
            self.start_state_set_inheritance(state_sets[state_set])

    def start_state_set_inheritance(self, state_set: StateSet):
        loop_transitions = []
        for transition in state_set.stablestate.setTrans:
            if transition.startState == transition.finalState and not transition.access:
                loop_transitions.append(transition)

        for start_state in state_set.startstates:
            for transition in loop_transitions:
                start_state.addtransitions(self._CopyModifyTransition(transition, start_state, start_state))

