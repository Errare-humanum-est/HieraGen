import copy

from typing import List, Dict
from Murphi.MurphiModular import MurphiModular

from DataObjects.ClassState import State
from DataObjects.ClassLevel import Level
from DataObjects.ClassTransition import Transition
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple

from Algorithms.HieraAlgorithm.HieraTransGen.HieraStateRenameGen import HieraStateRenameGen
from Algorithms.HieraAlgorithm.HieraTransGen.HieraMergeFunc import HieraMergeFunc


class LLAccessTransGen(HieraStateRenameGen, HieraMergeFunc):
    def __init__(self, low_level: Level, high_level: Level):
        HieraStateRenameGen.__init__(self)
        HieraMergeFunc.__init__(self)
        self.low_level = low_level
        self.high_level = high_level

    ####################################################################################################################
    # Access transition creation
    ####################################################################################################################

    def ll_cache_access_transitions(self, renamed_states: Dict[State, State],
                                    access_state_tuples: List[CcDirStateTuple]) -> List[Transition]:
        filtered_transition_list = {}
        for access_state_tuple in access_state_tuples:

            ll_dir_transitions = [copy.copy(trans) for trans in access_state_tuple.ll_dir_trace.transitions]
            hl_cc_transitions = [copy.copy(trans) for trans in access_state_tuple.hl_cc_trace.transitions]
            assert hl_cc_transitions[0].access, "hl cache has no access"

            # Label the current access as the high level access
            cur_access = hl_cc_transitions[0].access

            # rename transition states
            self.rename_dir_states(renamed_states, ll_dir_transitions, access_state_tuple.hl_cc_final_state)
            self.rename_cc_states(renamed_states, hl_cc_transitions, access_state_tuple.ll_dir_start_state)

            transition_list = self.conservative_ll_to_hl_merge(hl_cc_transitions, ll_dir_transitions)

            transition_list[0].access = cur_access

            # Finally clean up logical duplicates
            for transition in transition_list:
                # Check if a transition with the same start state, guards and messages already exists
                if transition.get_hash_ignore_finale_state() not in filtered_transition_list:
                    filtered_transition_list[transition.get_hash_ignore_finale_state()] = transition
                else:
                    found_equivalent_transition = filtered_transition_list[transition.get_hash_ignore_finale_state()]
                    cur_trans_index = transition_list.index(transition)
                    if cur_trans_index < len(transition_list) - 1:
                        # Update next transition final state
                        next_trans = transition_list[cur_trans_index + 1]
                        next_trans.startState = found_equivalent_transition.finalState
                    else:
                        # It is the final transition before entering the stable state
                        assert transition.finalState == found_equivalent_transition.finalState, \
                            "Protocol description is not consistent"

        return list(filtered_transition_list.values())

    def conservative_ll_to_hl_merge(self, hl_cc_transitions: List[Transition], ll_dir_transitions: List[Transition]):
        return self.conservative_level_merge(hl_cc_transitions,
                                             ll_dir_transitions,
                                             MurphiModular.tPUSH_LL_DEFER,
                                             MurphiModular.tPOP_LL_DEFER)
