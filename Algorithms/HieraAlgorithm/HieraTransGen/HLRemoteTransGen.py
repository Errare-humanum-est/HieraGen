import copy

from typing import List, Dict, Tuple
from Murphi.MurphiModular import MurphiModular

from DataObjects.ClassState import State
from DataObjects.ClassLevel import Level
from DataObjects.ClassTransition import Transition
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple

from Algorithms.HieraAlgorithm.HieraTransGen.HieraStateRenameGen import HieraStateRenameGen
from Algorithms.HieraAlgorithm.HieraTransGen.HieraMergeFunc import HieraMergeFunc

from antlr3.tree import CommonTree
from Algorithms.General.AuxStateHandler import AuxStateHandler
from Parser.ProtoCCcomTreeFct import toStringList

from Algorithms.HieraAlgorithm.ConcurrencyAnalysis import ConcurrencyAnalysis


class HLRemoteTransGen(HieraStateRenameGen, HieraMergeFunc, ConcurrencyAnalysis):
    def __init__(self, low_level: Level, high_level: Level):
        HieraStateRenameGen.__init__(self)
        HieraMergeFunc.__init__(self)
        ConcurrencyAnalysis.__init__(self, low_level)
        self.low_level = low_level
        self.high_level = high_level

    ####################################################################################################################
    # Remote access transition
    ####################################################################################################################
    def hl_cache_remote_transitions(self, renamed_states: Dict[State, State],
                                    remote_state_tuples: List[CcDirStateTuple]) -> List[Transition]:
        cache_transitions = []
        for remote_state_tuple in remote_state_tuples:
            trace_cache_transitions = []

            assert remote_state_tuple.ll_proxy_trace, "Error no proxy trace found for remote access transition generation"

            transaction_sequences = self.hl_cache_remote_concurrency_analysis(remote_state_tuple)
            if not transaction_sequences:
                continue
            transaction_sequences = self.generate_proxy_dir_transactions(transaction_sequences)

            trace_cache_transitions += self.hl_cache_remote_proxy_transition(renamed_states,
                                                                             remote_state_tuple,
                                                                             transaction_sequences)

            # Remove duplicates
            for trace_cache_transition in trace_cache_transitions:
                cache_transition_hash_list = [trans.get_hash() for trans in cache_transitions]
                if trace_cache_transition.get_hash() not in cache_transition_hash_list:
                    cache_transitions.append(trace_cache_transition)
                else:
                    assert "DUPLICATES"

        return cache_transitions

    def hl_cache_remote_proxy_transition(self,
                                         renamed_states: Dict[State, State],
                                         evict_state_tuple: CcDirStateTuple,
                                         proxy_dir_transaction_blocks: List[List[Transition]]) -> List[Transition]:

        hl_cc_transitions = [copy.copy(trans) for trans in evict_state_tuple.hl_cc_trace.transitions]
        ll_proxy_dir_access_transitions = [copy.copy(trans) for trans in proxy_dir_transaction_blocks[0]]
        ll_proxy_dir_evict_transitions = [copy.copy(trans) for trans in proxy_dir_transaction_blocks[1]]

        dir_trans = self.chain_transitions(ll_proxy_dir_access_transitions, ll_proxy_dir_evict_transitions)

        # Only ll_dir response messages that have a data dependency with the hl_cache response messages are deferred
        dir_trans[0].access = ""
        # rename transition states
        self.rename_dir_states(renamed_states, dir_trans, evict_state_tuple.hl_cc_start_state)
        self.rename_cc_states(renamed_states, hl_cc_transitions, evict_state_tuple.ll_dir_final_state)

        transition_list = self.conservative_hl_to_ll_merge(dir_trans, hl_cc_transitions)

        # The directory behaves like a cache, so it inherits the access_classification of the cache side
        dir_trans[0].access_class = hl_cc_transitions[0].access_class
        dir_trans[0].comm_class = hl_cc_transitions[0].comm_class

        return transition_list

    # Create proxy dir controller transitions
    def generate_proxy_dir_transactions(self, transition_sequences_list: List[List[Transition]]) \
            -> List[List[Transition]]:
        proxy_dir_transition_sequences_list: List[List[Transition]] = []
        for transition_sequence in transition_sequences_list:
            proxy_dir_transition_sequences_list.append(self.merge_proxy_dir_transitions(transition_sequence))

        #assert len(proxy_dir_transition_sequences_list) == 2, "Print to many transitions in remote access sequence"

        return proxy_dir_transition_sequences_list

    def merge_proxy_dir_transitions(self, proxy_dir_transitions: List[Transition]) -> List[Transition]:
        # Move copy here
        cur_transitions = proxy_dir_transitions
        merge_found = 1
        while merge_found:
            merge_found = 0
            new_cur_transitions = []
            for transition_ind in range(0, len(cur_transitions)):
                prev_transition = cur_transitions[transition_ind]
                if transition_ind + 1 < len(cur_transitions):
                    next_transition = cur_transitions[transition_ind + 1]
                    merged_transition = self.try_merge_proxy_dir_transition(prev_transition, next_transition)

                    if merged_transition:
                        merge_found = 1
                        new_cur_transitions.append(merged_transition)
                        next_trans_ind = cur_transitions.index(next_transition) + 1
                        if next_trans_ind < len(cur_transitions):
                            new_cur_transitions += cur_transitions[next_trans_ind:len(cur_transitions)]
                        break

                new_cur_transitions.append(prev_transition)
            cur_transitions = new_cur_transitions

        return cur_transitions

    def try_merge_proxy_dir_transition(self, prev_transition: Transition, next_transition: Transition) -> Transition:
        prev_transition = prev_transition.deepcopy_modify_trans_except_states()
        next_transition = next_transition.deepcopy_modify_trans_except_states()

        inmsg_str = str(next_transition.inMsg)
        outmsg_str_list = [str(transition) for transition in prev_transition.outMsg]
        if inmsg_str not in outmsg_str_list:
            return None
        else:
            # remove index from outMsg list
            remove_msg = prev_transition.outMsg.pop(outmsg_str_list.index(inmsg_str))

        remove_operation = self.find_assign_msg_by_str(remove_msg, prev_transition)
        msg_var_name = str(remove_operation[0].children[0])
        msg_name = str(remove_operation[1][0])
        new_msg_var_name = msg_var_name + "_" + msg_name
        remove_send_func = self.remove_send_func(remove_operation[0], prev_transition)

        # Update the variable name to avoid it to be overwritten
        AuxStateHandler.save_rename_var(prev_transition.operation, remove_operation[0], msg_var_name, new_msg_var_name)

        # Update all operations that were using the previously received message
        # Reassign variable in output function
        AuxStateHandler.cond_operations_var_rename(next_transition.operation,
                                                   str(remove_operation[1][0]),
                                                   new_msg_var_name)

        # Update missing inmessage assignment in next transition
        prev_transition.operation += next_transition.operation
        prev_transition.outMsg += next_transition.outMsg
        prev_transition.cond += next_transition.cond

        prev_transition.finalState = next_transition.finalState

        return prev_transition

    @staticmethod
    def find_assign_msg_by_str(msg_str: str, transition: Transition) -> Tuple[CommonTree, List[CommonTree]]:
        for operation in transition.operation:
            children = operation.children
            if str(operation) == MurphiModular.tASSIGN and str(children[2]) == MurphiModular.tMSGCSTR:
                if str(msg_str) in toStringList(children[2]):
                    return operation, [children[2].children[1]]

    def remove_send_func(self, assign_operation: CommonTree, transition: Transition) -> CommonTree:
        msg_var_name = str(assign_operation.children[0])
        var_assigned: bool = False
        for operation in transition.operation:
            if id(operation) == id(assign_operation):
                var_assigned = True
            if var_assigned and str(operation) == MurphiModular.tSEND:
                if str(operation.children[1]) == str(msg_var_name):
                    return transition.operation.pop(transition.operation.index(operation))

    def chain_transitions(self, prev_transitions: List[Transition], next_transitions: List[Transition]) -> List[Transition]:
        new_trans_sequence = prev_transitions
        prev_transition = prev_transitions[-1]
        next_transition = next_transitions[0]
        prev_transition.cond = prev_transition.cond + next_transition.cond
        prev_transition.operation = prev_transition.operation + next_transition.operation
        prev_transition.outMsg = prev_transition.outMsg + next_transition.outMsg
        prev_transition.finalState = next_transition.finalState

        # Serve remaining directory transitions
        for trans_ind in range(1, len(next_transitions)):
            new_trans_sequence.append(next_transitions[trans_ind])

        return new_trans_sequence

    def conservative_hl_to_ll_merge(self, ll_dir_transitions: List[Transition], hl_cc_transitions: List[Transition]):
        return self.conservative_level_merge(ll_dir_transitions,
                                             hl_cc_transitions,
                                             MurphiModular.tPUSH_HL_DEFER,
                                             MurphiModular.tPOP_HL_DEFER)
