import copy
from typing import Dict, List

from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple

from Algorithms.HieraAlgorithm.HieraTransGen.HieraStateRenameGen import HieraStateRenameGen


class LLEvictTransGen(HieraStateRenameGen):

    def __init__(self):
        HieraStateRenameGen.__init__(self)

    ####################################################################################################################
    # LL evict
    ####################################################################################################################
    def ll_cache_evict_transitions(self, renamed_states: Dict[State, State],
                                   evict_state_tuples: List[CcDirStateTuple]) -> List[Transition]:
        cache_transitions = []

        for evict_state_tuple in evict_state_tuples:

            ll_dir_transitions = []
            hl_cc_transitions = []

            if evict_state_tuple.ll_dir_trace:
                ll_dir_transitions = [copy.copy(trans) for trans in evict_state_tuple.ll_dir_trace.transitions]

            if evict_state_tuple.hl_cc_trace:
                hl_cc_transitions = [copy.copy(trans) for trans in evict_state_tuple.hl_cc_trace.transitions]

            # rename transition states
            if hl_cc_transitions:
                self.rename_cc_states(renamed_states, hl_cc_transitions, evict_state_tuple.ll_dir_final_state)
            if ll_dir_transitions:
                self.rename_dir_states(renamed_states, ll_dir_transitions, evict_state_tuple.hl_cc_final_state)

            assert not (ll_dir_transitions and hl_cc_transitions), \
                "Evictions show dependence on other hierachical layer"

            cache_transitions += ll_dir_transitions
            cache_transitions += hl_cc_transitions

        return cache_transitions

