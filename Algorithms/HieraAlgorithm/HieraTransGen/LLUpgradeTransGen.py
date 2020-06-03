import copy

from typing import List, Dict
from Murphi.MurphiModular import MurphiModular

from DataObjects.ClassState import State
from DataObjects.ClassLevel import Level
from DataObjects.ClassTransition import Transition
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple

from Algorithms.HieraAlgorithm.HieraTransGen.HieraStateRenameGen import HieraStateRenameGen
from Algorithms.HieraAlgorithm.HieraTransGen.HieraMergeFunc import HieraMergeFunc

from Algorithms.General.AuxStateHandler import AuxStateHandler


class LLUpgradeTransGen(HieraStateRenameGen, HieraMergeFunc):
    internal_msg = "internal_msg_dummy"

    def __init__(self, low_level: Level, high_level: Level):
        HieraStateRenameGen.__init__(self)
        HieraMergeFunc.__init__(self)
        self.low_level = low_level
        self.high_level = high_level

    ####################################################################################################################
    # Access transition creation
    ####################################################################################################################

    def ll_cache_upgrade_transitions(self, renamed_states: Dict[State, State],
                                    upgrade_state_tuples: List[CcDirStateTuple]) -> List[Transition]:
        filtered_transition_list = {}

        for upgrade_state_tuple in upgrade_state_tuples:

            # Generate precharge transition sequence
            precharge_proxy_tuple = CcDirStateTuple(upgrade_state_tuple.ll_dir_trace.orig_traces[0],
                                                None,
                                                upgrade_state_tuple.ll_proxy_trace.orig_traces[0])
            precharge_proxy_sequence = self.hl_cache_remote_concurrency_analysis(precharge_proxy_tuple)
            precharge_proxy_sequence = self.generate_proxy_dir_transactions(precharge_proxy_sequence)[0]

            # Temporarily rename internal GetS message so it does not get renamed in the merging process, being
            # confused with the ll requestor message
            for transition in precharge_proxy_sequence:
                for out_msg in upgrade_state_tuple.ll_proxy_trace.orig_traces[0].outmsg:
                    AuxStateHandler.cond_operations_var_rename(transition.operation, out_msg, out_msg + self.internal_msg)

            # Serve ll cache request after precharging is complete
            ll_access_dir_transitions = [copy.copy(trans) for trans in upgrade_state_tuple.ll_dir_trace.orig_traces[1].transitions]
            ll_access_proxy_transitions = [copy.copy(trans) for trans in upgrade_state_tuple.ll_proxy_trace.orig_traces[1].transitions]
            ll_access_dir_response_transitions = []
            if len(ll_access_dir_transitions) > 1:
                ll_access_dir_response_transitions = ll_access_dir_transitions[1:]

            ll_access_dir_transitions = [[ll_access_dir_transitions[0]]
                                         + ll_access_proxy_transitions
                                         + ll_access_dir_response_transitions]

            proxy_access_transitions = self.generate_proxy_dir_transactions(ll_access_dir_transitions)[0]

            # Generate the evict sequence
            evict_proxy_tuple = CcDirStateTuple(upgrade_state_tuple.ll_dir_trace.orig_traces[2],
                                                None,
                                                upgrade_state_tuple.ll_proxy_trace.orig_traces[2])
            evict_proxy_sequence = self.hl_cache_remote_concurrency_analysis(evict_proxy_tuple)
            evict_proxy_sequence = self.generate_proxy_dir_transactions(evict_proxy_sequence)[0]

            first_trans_sequence = self.chain_transitions(precharge_proxy_sequence, proxy_access_transitions)
            ll_cache_dir_transitions: List[Transition] = \
                self.chain_transitions(first_trans_sequence, evict_proxy_sequence)

            ll_cache_dir_transitions[0].inMsg = proxy_access_transitions[0].inMsg
            ll_cache_dir_transitions[0].access = ""
            ll_cache_dir_transitions[0].comm_class = proxy_access_transitions[0].comm_class

            hl_cc_transitions = [copy.copy(trans) for trans in upgrade_state_tuple.hl_cc_trace.transitions]
            assert hl_cc_transitions[0].access, "hl cache has no access"

            # rename transition states
            self.rename_dir_states(renamed_states, ll_cache_dir_transitions, upgrade_state_tuple.hl_cc_final_state)
            self.rename_cc_states(renamed_states, hl_cc_transitions, upgrade_state_tuple.ll_dir_start_state)

            transition_list = self.conservative_ll_to_hl_merge(hl_cc_transitions, ll_cache_dir_transitions)

            transition_list[0].access = upgrade_state_tuple.ll_access_cc_trace.access[0]

            # Undo the message renaming of the internal dummy messages
            for transition in precharge_proxy_sequence:
                for out_msg in upgrade_state_tuple.ll_proxy_trace.orig_traces[0].outmsg:
                    AuxStateHandler.cond_operations_var_rename(transition.operation, out_msg + self.internal_msg, out_msg)

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
