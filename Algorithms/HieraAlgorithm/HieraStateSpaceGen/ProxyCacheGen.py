from typing import List, Tuple, Dict

from DataObjects.ClassState import State
from DataObjects.ClassLevel import Level
from DataObjects.ClassTransition import Transition
from Algorithms.General.Tracing.TraceTree import Trace

from Algorithms.HieraAlgorithm.HieraStateSpaceGen.StateTupleBaseFunc import StateTupleBaseFunc
from DataObjects.ClassSystemTuple import SystemTuple


class ProxyCacheGen(StateTupleBaseFunc):
    def __init__(self, low_level: Level, high_level: Level):
        StateTupleBaseFunc.__init__(self)
        self.low_level = low_level
        self.high_level = high_level

    def ll_find_proxy_traces(self, hl_dir_trace: Trace, ll_dir_state: State):
        # proxy, dir
        ll_proxy_dir_trace_tuples: Dict[SystemTuple, SystemTuple] = {}

        # High level directory state maximum associated access
        hl_dir_state_classification = self.high_level.dir_access_classification_map[hl_dir_trace.finalstate]
        remote_access = hl_dir_state_classification.immed_access[-1]

        # Extract all ll_proxy_cache_transitions whose final state has the same permissions
        # Proxy cache is initially in state I
        for state_tuple in self.low_level.state_tuple_list:
            # Extract the directory trace
            ll_dir_trace = self.get_dir_trace(state_tuple, self.low_level)

            # If the start state of the directory trace does not match the current convoluted dir state
            # or no directory trace is found -> continue
            if not ll_dir_trace or ll_dir_trace.startstate != ll_dir_state:  # desired directory start state
                continue

            ll_access_trace = self.get_cache_access_trace(state_tuple, self.low_level)

            # If an access trace exists and the access trace contains load or store (not evict)
            if not ll_access_trace or ll_access_trace.access[0] != remote_access:
                continue

            if ll_access_trace.startstate != self.low_level.cache.init_state:
                continue

            # The final state ll directory state must have as strong access permissions as the hl directory state
            ll_dir_state_classification = self.low_level.dir_access_classification_map[ll_dir_trace.finalstate]

            # Requested directory final state is not strong enough
            if not hl_dir_state_classification <= ll_dir_state_classification:
                continue

            # Additional safety check that the proxy cache access permission is strong enough
            ll_state_class = self.low_level.cache.state_classification[ll_access_trace.finalstate]

            # Requested directory final state is not strong enough
            if not hl_dir_state_classification <= ll_state_class:
                continue

            ll_proxy_dir_trace_tuples[state_tuple] = state_tuple

        return ll_proxy_dir_trace_tuples

    # Two level optimization
    # If a known state tuple is recognized and that matches the remote proxy request then the state tuple function finds
    # a correct eviction pattern. If that is not the case, the ll_extract_evict_no_state_tuple function brute forces all
    # evictions that could fit the purpose and adds them as edges. This however, can result in unreachable edges and
    # reduces optimality of solution
    def _ll_extract_evict(self, proxy_trace: Trace, dir_trace: Trace, hl_remote_trace: Trace = None):
        # proxy, dir
        evict_traces: List[Tuple[Trace, Trace]] = []
        for state_tuple in self.low_level.state_tuple_list:
            # find cache evict trace
            ll_access_trace = self.get_cache_access_trace(state_tuple, self.low_level)
            if not ll_access_trace:
                continue

            if ll_access_trace.startstate != proxy_trace.finalstate:
                continue

            if ll_access_trace.access != proxy_trace.finalstate.evict:
                continue

            ll_dir_trace = self.get_dir_trace(state_tuple, self.low_level)

            if not ll_dir_trace:
                ll_dir_trace = self.dummy_trace(dir_trace.finalstate)
            elif ll_dir_trace.startstate != dir_trace.finalstate:
                continue

            evict_traces.append((ll_access_trace, ll_dir_trace))

        if not evict_traces and hl_remote_trace:
            # Due to concurrency the eviction state is not determined yet, a set of possible outcomes needs to be
            # considered as no state tuple exists
            evict_traces += self._ll_extract_evict_no_state_tuple(proxy_trace, dir_trace, hl_remote_trace)

        return evict_traces

    def _ll_extract_evict_no_state_tuple(self, proxy_trace: Trace, dir_trace: Trace, hl_remote_trace: Trace):
        evict_traces: List[Tuple[Trace, Trace]] = []
        for ll_cache_trace in self.low_level.cache.traces.start_state_dict[proxy_trace.finalstate]:

            if not [access for access in ll_cache_trace.access if access in proxy_trace.finalstate.evict]:
                continue

            # Check whether access permission is weak enough
            ll_cache_state_class = self.low_level.cache.state_classification[ll_cache_trace.finalstate]
            hl_cache_state_class = self.high_level.cache.state_classification[hl_remote_trace.finalstate]

            # Requested state is strong enough
            if not ll_cache_state_class <= hl_cache_state_class:
                continue

            for ll_dir_trace in self.low_level.directory.traces.start_state_dict[dir_trace.finalstate]:

                if not [outmsg for outmsg in ll_cache_trace.outmsg if str(outmsg) in ll_dir_trace.inmsg]:
                    continue

                ll_dir_state_class = self.low_level.dir_access_classification_map[ll_dir_trace.finalstate]

                if not ll_dir_state_class <= hl_cache_state_class:
                    continue

                evict_traces.append((ll_cache_trace, ll_dir_trace))

        return evict_traces

    def dummy_trace(self, state: State):
        trans = Transition(state, state)
        return Trace.constr_trace_from_trans(trans)
