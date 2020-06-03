import copy
from typing import List, Union

from DataObjects.ClassLevel import Level
from DataObjects.ClassTransition import Transition

from Parser.ForkTree import ForkTree

from Algorithms.General.Tracing.TraceNode import TraceNodeObj
from Algorithms.General.Tracing.TraceTree import Trace

from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple


class ConcurrencyAnalysis:
    def __init__(self, low_level: Level):
        self.low_level = low_level

    ''' 
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Analyze the possible concurrency of response messages to a single controller
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ####################################################################################################################
    # CONCURRENCY ANALYSIS
    ####################################################################################################################
    '''
    # Create tree of concurrent transitions competing (Improve using message destinations in the future...
    def hl_cache_remote_concurrency_analysis(self, evict_state_tuple: CcDirStateTuple) -> List[List[Transition]]:
        trace_cache_transitions = []

        #assert len(evict_state_tuple.ll_proxy_trace.orig_traces) == len(evict_state_tuple.ll_dir_trace.orig_traces), \
        #    "Proxy cache and dir transaction count mismatch"

        for transaction_ind in range(0, len(evict_state_tuple.ll_proxy_trace.orig_traces)):
            cache_transition_sequences = []
            ll_proxy_trace = evict_state_tuple.ll_proxy_trace.orig_traces[transaction_ind]
            ll_dir_trace = evict_state_tuple.ll_dir_trace.orig_traces[transaction_ind]
            ll_remote_traces_list = self.find_state_tuple(ll_proxy_trace, ll_dir_trace)

            # Introduces concurrency to avoid deadlocks
            if ll_remote_traces_list:
                for ll_remote_traces in ll_remote_traces_list:
                    cache_transition_sequences += self.ll_proxy_dir_trace(ll_dir_trace,
                                                                          ll_proxy_trace,
                                                                          ll_remote_traces)
            elif ll_dir_trace.inmsg or ll_dir_trace.outmsg or ll_dir_trace.access:
                cache_transition_sequences += self.ll_proxy_dir_trace(ll_dir_trace,
                                                                      ll_proxy_trace,
                                                                      None)
            elif len(ll_proxy_trace.transitions) == 1:      # The directory transition is a dummy transition
                cache_transition_sequences += [ll_proxy_trace.transitions]

            if not cache_transition_sequences:
                return []

            # remove duplicate transitions lists....
            new_cache_transition_sequences = []
            for cache_transition_sequence in cache_transition_sequences:
                found = 0
                for new_cache_transition_sequence in new_cache_transition_sequences:
                    hash_new = [transition.get_hash() for transition in new_cache_transition_sequence]
                    hash_cur = [transition.get_hash() for transition in cache_transition_sequence]
                    if hash_new == hash_cur:
                        found = 1
                        break

                if not found:
                    new_cache_transition_sequences.append(cache_transition_sequence)

            proxy_dir_transitions = []
            for new_cache_transition_sequence in new_cache_transition_sequences:
                proxy_dir_transitions.append(self.update_transaction_states(ll_dir_trace,
                                                                            evict_state_tuple.hl_cc_trace,
                                                                            new_cache_transition_sequence))

            if len(proxy_dir_transitions) > 1:
                print("multiple path detected")
                assert "ANALYZE"
            if proxy_dir_transitions:
                trace_cache_transitions += proxy_dir_transitions

        return trace_cache_transitions

    def update_transaction_states(self, ll_dir_trace: Trace,
                                  hl_cc_trace: Trace,
                                  transitions: List[Transition]):
        # During the remote access, no more directory state requests must be served
        new_transitions = []
        # Rename directory states
        dir_start_state = copy.copy(ll_dir_trace.transitions[0].startState)
        dir_final_state = copy.copy(ll_dir_trace.transitions[-1].finalState)

        cur_start_state = dir_start_state
        for ind_trans in range(0, len(transitions)):
            transition = copy.copy(transitions[ind_trans])

            if transition.getaccess() and hl_cc_trace:
                access_str = str(hl_cc_trace.inmsg[0]) + "_" + transition.getaccess()
            else:
                access_str = str(transition.getinmsg())

            transition.startState = cur_start_state

            if ind_trans < len(transitions) - 1:
                next_start_state = copy.copy(transitions[ind_trans + 1].startState)
                next_start_state.state = cur_start_state.state + "_" + access_str
            else:
                next_start_state = dir_final_state

            transition.finalState = next_start_state

            cur_start_state = next_start_state

            new_transitions.append(transition)

        return new_transitions

    ####################################################################################################################
    # Transition sequence tree generation (Required to determine sequence of cache and directory transactions)
    # sequence of cache and directory transactions is required to avoid deadlocks in case of dependencies
    # E.G. Remote cache sends two responses which possibly can be reordered. Also possible multiple caches
    # send responses to the cache and to the directory, all possible interleavings of the responses
    # need to be considered
    ####################################################################################################################
    def ll_proxy_dir_trace(self, ll_dir_trace: Trace, ll_proxy_trace: Trace,
                           ll_remote_traces: Union[List[Trace], None]) -> List[List[Transition]]:
        cache_transitions = []
        ll_dir_transistions = [copy.copy(trans) for trans in ll_dir_trace.transitions]
        ll_prox_transitions = [copy.copy(trans) for trans in ll_proxy_trace.transitions]

        ll_remote_transitions = []
        if ll_remote_traces:
            for ll_remote_trace in ll_remote_traces:
                if ll_remote_trace:
                    ll_remote_transitions += [copy.copy(trans) for trans in ll_remote_trace.transitions]

        trace_tree = ForkTree()

        basenode = trace_tree.insertnode(TraceNodeObj(ll_prox_transitions[0].outMsg, ll_prox_transitions[0]))
        nextlist = self.get_next_transitions([basenode],
                                             ll_dir_transistions, ll_prox_transitions, ll_remote_transitions)

        while nextlist:
            endnodes = []
            for nextnode in nextlist:
                endnodes += trace_tree.appenddata(nextnode[1], nextnode[0])

            nextlist = []
            for node in endnodes:
                nextlist += self.get_next_transitions([node],
                                                      ll_dir_transistions, ll_prox_transitions, ll_remote_transitions)

        new_traces = trace_tree.gettraces()

        # Check the length of each trace and remove to short traces, brute force state exploration
        # sort out traces that are too short indicating that not all traces have been used
        valid_traces = []
        for new_trace in new_traces:
            trans_sequence = [node.transition for node in new_trace]
            # Convert to standard trace
            if set(ll_dir_transistions + ll_prox_transitions).issubset(set(trans_sequence)):
                valid_traces.append(new_trace)

        # convert traces into transitions
        for valid_trace in valid_traces:
            cache_transitions.append(self.convert_traces_to_cc_dir_transition_traces_list(valid_trace,
                                                                                          ll_remote_transitions))
        return cache_transitions

    def get_next_transitions(self, nodes, ll_dir_transistions: List[Transition],
                             ll_prox_transitions: List[Transition],
                             ll_remote_transitions: List[Transition],
                             concurrency=False):
        nextlist = []

        remote_msg_sequence = []

        msg_tuples = []
        for trans in ll_remote_transitions:
            msg_tuples.append(tuple([str(outmsg) for outmsg in trans.getoutmsg()]))

        # and not refers to multiple caches sending two responses... then concurrency must be considered again
        if len(set(msg_tuples)) == 1 and not (len(msg_tuples[0]) > 1 and len(msg_tuples) > 1):
            remote_msg_sequence = msg_tuples[0]
            concurrency = False

        for node in nodes:
            nextstates = []

            served_transitions = self.extract_prev_transitions(node)
            outmsg_list = self.extract_pending_out_msg(served_transitions)
            next_transitions = self.find_next_ready_transition(served_transitions, ll_dir_transistions) + \
                               self.find_next_ready_transition(served_transitions, ll_prox_transitions) + \
                               self.find_next_ready_transition(served_transitions, ll_remote_transitions)

            sel_remote = False
            # First outmsg must be checked to ensure ordering is maintained of responses
            for outmsg in outmsg_list:
                for transition in next_transitions:
                    if str(transition.inMsg) == str(outmsg):

                        # Condition check to avoid artificial introduction of concurrency in ordered networks
                        if (outmsg in remote_msg_sequence) and not concurrency and sel_remote:
                            continue

                        nextstates.append(TraceNodeObj(transition.outMsg, transition))

                        # A remote transition was selected
                        if (outmsg in remote_msg_sequence):
                            sel_remote = True

            #if not nextstates and not ll_remote_transitions:
            #    dir_next_transitions = self.find_next_ready_transition(served_transitions, ll_dir_transistions)
            #    if dir_next_transitions:
            #        nextstates.append(TraceNodeObj(transition.outMsg, transition))

            nextlist.append([node, nextstates])

        return nextlist

    @staticmethod
    def extract_prev_transitions(node: 'Node'):
        served_transitions = []
        prev_node = node
        while prev_node:
            served_transitions.append(prev_node.getdata().get_transition())
            prev_node = prev_node.getpredecessor()
        served_transitions.reverse()
        return served_transitions

    @staticmethod
    def extract_pending_out_msg(transitions: List[Transition]) -> List[str]:
        in_msgs = []
        out_msgs = []
        for transition in transitions:
            in_msgs.append(transition.inMsg)
            out_msgs += transition.outMsg

        in_msgs = [str(in_msg) for in_msg in in_msgs]
        out_msgs = [str(out_msg) for out_msg in out_msgs] + ['']

        assert set(in_msgs).issubset(set(out_msgs)), "In message mismatch transitions"

        # Return messages ordered
        ret_msg = []
        for out_msg in out_msgs:
            if out_msg not in in_msgs and out_msg not in ret_msg:
                ret_msg.append(out_msg)

        return ret_msg

    @staticmethod
    def find_next_ready_transition(served_transitions: List[Transition],
                                   ref_transitions: List[Transition]) -> List[Transition]:
        if not ref_transitions:
            return []

        max_ind = -1
        for transition in served_transitions:
            if transition in ref_transitions:
                cur_index = ref_transitions.index(transition)
                if cur_index > max_ind:
                    max_ind = cur_index

        if max_ind < len(ref_transitions) - 1:
            return [ref_transitions[max_ind + 1]]
        return []

    @staticmethod
    def convert_traces_to_cc_dir_transition_traces_list(trace: Trace,
                                                        ll_remote_transitions: List[Transition]) -> List[Transition]:
        cc_dir_transitions = []
        for node in trace:
            if node.transition not in ll_remote_transitions:
                cc_dir_transitions.append(node.transition)
        cc_dir_transitions.reverse()
        return cc_dir_transitions

    def find_state_tuple(self, proxy_cache_trace: Trace, ll_dir_trace: Trace) -> [List[List[Trace]], None]:
        remote_cache_traces: List[List[Trace]] = []
        # Explore all possible state combinations
        for state_tuple in self.low_level.state_tuple_list:

            cur_ll_dir_trace = state_tuple.get_arch_traces(self.low_level.directory)
            if not ll_dir_trace.comp_trace_list(cur_ll_dir_trace):
                continue

            cur_ll_cc_trace = state_tuple.get_arch_access_trace(self.low_level.cache)
            if not proxy_cache_trace.comp_trace_list(cur_ll_cc_trace):
                continue

            remote_cache_traces.append(list(set(state_tuple.get_arch_remote_trace(self.low_level.cache))))

        return remote_cache_traces
    # End concurrency analysis
