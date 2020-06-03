from typing import List, Tuple, Dict

from DataObjects.ClassState import State
from DataObjects.ClassLevel import Level
from Algorithms.General.Tracing.TraceTree import Trace
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple

from Algorithms.HieraAlgorithm.HieraStateSpaceGen.ProxyCacheGen import ProxyCacheGen
from DataObjects.ClassSystemTuple import SystemTuple


class HLRemoteStateGen(ProxyCacheGen):
    def __init__(self, low_level: Level, high_level: Level):
        ProxyCacheGen.__init__(self, low_level, high_level)
        self.low_level = low_level
        self.high_level = high_level

        self.legacy_proxy_function = False

    """
    ####################################################################################################################
    ##### Remote request implementation HL to LL
    ####################################################################################################################
    """
    def remote_traces(self, state_tuple: List[Tuple[State, State]]) -> List[CcDirStateTuple]:
        remote_req_tuples: Dict[CcDirStateTuple, CcDirStateTuple] = {}

        for state_set in state_tuple:
            for hl_state_tuple in self.high_level.state_tuple_list:
                hl_remote_traces = self.get_cache_remote_trace(hl_state_tuple, self.high_level)
                # Recover traces from remote_traces list that have the right start state
                hl_remote_traces = [remote_trace for remote_trace in hl_remote_traces
                                    if remote_trace.startstate == state_set[1]]
                if not hl_remote_traces:
                    continue

                # recover access
                hl_access_trace = self.get_cache_access_trace(hl_state_tuple, self.high_level)
                assert len(hl_access_trace.access) <= 1, "HieraGen unable to handle more than one cache access"
                hl_dir_trace = self.get_dir_trace(hl_state_tuple, self.high_level)

                # proxy, dir
                if self.legacy_proxy_function:
                    ll_proxy_dir_trace_tuples = ProxyCacheGen.ll_find_proxy_traces(hl_dir_trace, state_set[0])
                else:
                    # Experimental
                    ll_proxy_dir_trace_tuples = self.ll_find_proxy_traces(hl_dir_trace,
                                                                                 state_set[0])
                    ll_proxy_dir_trace_tuples = self.extract_proxy_dir_traces(ll_proxy_dir_trace_tuples)

                # proxy access evict combinations
                for ll_proxy_dir_trace_tuple in ll_proxy_dir_trace_tuples:
                    for hl_remote_trace in hl_remote_traces:
                        # iterate over the remote traces, there can be multiple remote traces with the same guard,
                        # because of different auxiliary conditions
                        ll_proxy_dir_evict_traces = self._ll_extract_evict(*ll_proxy_dir_trace_tuple, hl_remote_trace)
                        if ll_proxy_dir_evict_traces:
                            for ll_proxy_dir_evict_trace in ll_proxy_dir_evict_traces:

                                hash_id = self._calculate_hash(hl_remote_trace,
                                                               ll_proxy_dir_trace_tuple[0],
                                                               ll_proxy_dir_trace_tuple[1],
                                                               ll_proxy_dir_evict_trace[0],
                                                               ll_proxy_dir_evict_trace[1])

                                new_tuple = CcDirStateTuple(ll_proxy_dir_trace_tuple[1] + ll_proxy_dir_evict_trace[1],
                                                            hl_remote_trace,
                                                            ll_proxy_dir_trace_tuple[0] + ll_proxy_dir_evict_trace[0],
                                                            hl_access_trace)

                                remote_req_tuples[hash_id] = new_tuple

        return list(remote_req_tuples.values())

    def _calculate_hash(self,
                        hl_cc_trace: Trace,
                        ll_proxy_trace: Trace,
                        ll_dir_trace: Trace,
                        ll_proxy_cache_evict_trace: Trace,
                        ll_proxy_dir_evict_trace: Trace) -> int:
        trace_tuple = (hl_cc_trace.trans_hash(), ll_proxy_trace.trans_hash(), ll_dir_trace.trans_hash(),
                       ll_proxy_cache_evict_trace.trans_hash(), ll_proxy_dir_evict_trace.trans_hash())
        return hash(trace_tuple)

    def extract_proxy_dir_traces(self, system_state_tuples: Dict[SystemTuple, SystemTuple]) -> \
            Dict[Tuple[Trace, Trace], Tuple[Trace, Trace]]:
        ll_proxy_dir_trace_tuples: Dict[Tuple[Trace, Trace], Tuple[Trace, Trace]] = {}
        for system_state_tuple in system_state_tuples:
            ll_proxy_access_trace = self.get_cache_access_trace(system_state_tuple, self.low_level)
            ll_dir_access_trace = self.get_dir_trace(system_state_tuple, self.low_level)
            new_tuple = (ll_proxy_access_trace, ll_dir_access_trace)
            ll_proxy_dir_trace_tuples[new_tuple] = new_tuple

        return ll_proxy_dir_trace_tuples
