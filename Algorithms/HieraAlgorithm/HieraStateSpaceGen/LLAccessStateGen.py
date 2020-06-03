from typing import List, Tuple, Dict

from DataObjects.ClassState import State
from DataObjects.ClassLevel import Level
from Algorithms.General.Tracing.TraceTree import Trace
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple

from Algorithms.HieraAlgorithm.HieraStateSpaceGen.ProxyCacheGen import ProxyCacheGen
from Algorithms.HieraAlgorithm.HieraStateTupleClass.StateClassification import StateClassification


class LLAccessStateGen(ProxyCacheGen):
    def __init__(self, low_level: Level, high_level: Level):
        ProxyCacheGen.__init__(self, low_level, high_level)
        self.low_level = low_level
        self.high_level = high_level

        self._access_state_tuples: Dict[CcDirStateTuple, CcDirStateTuple] = {}
        self._silent_upgrade_state_tuples: Dict[Tuple[Trace], CcDirStateTuple] = {}

        self.access_state_tuples: List[CcDirStateTuple] = []
        self.upgrade_state_tuples: List[CcDirStateTuple] = []

        '''
        pessimistic_access: If true and lower level has silent upgrades, the higher level must have acquired 
        the cache line with the required immediate access permissions. 
        '''
        self.pessimistic_access = False

        '''
        inclusive_relaxation: Inclusiveness of higher level to lower level must be relaxed if using the TSO protocol
        '''
        self.inclusive_relaxation = False

    """
    ####################################################################################################################
    ##### Access request implementation LL to HL
    ####################################################################################################################
    """
    def access_traces_top_down(self, state_tuple: List[Tuple[State, State]]):
        for state_set in state_tuple:

            for state_tuple in self.low_level.state_tuple_list:
                # Extract the directory trace
                ll_dir_trace = self.get_dir_trace(state_tuple, self.low_level)

                # If the start state of the directory trace does not match the current convoluted dir state
                # or no directory trace is found -> continue
                if not ll_dir_trace or ll_dir_trace.startstate != state_set[0]:  # desired directory start state
                    continue

                ll_access_trace = self.get_cache_access_trace(state_tuple, self.low_level)

                # If an access trace exists and the access trace contains load or store (not evict)
                if not ll_access_trace or not ll_access_trace.access[0] in self.low_level.cache.init_state.access:
                    continue

                self._hl_extract_access(ll_access_trace, ll_dir_trace, state_set[1])

        self.access_state_tuples = list(self._access_state_tuples.values())
        self.upgrade_state_tuples = list(self._silent_upgrade_state_tuples.values())

    def _hl_extract_access(self, ll_access_trace: Trace, ll_dir_trace: Trace, hl_cc_state: State):
        hl_traces = []

        access_list = self.high_level.cache.init_state.access

        # Get minimum access request to outside world
        if self.pessimistic_access:
            final_state_max_access = self.low_level.cache.state_classification[ll_access_trace.finalstate]
            base_access_ind = access_list.index(final_state_max_access.immed_access[-1])
        else:
            base_access_ind = access_list.index(ll_access_trace.access[0])

        assert len(ll_access_trace.access) <= 1, "HieraGen unable to handle more than one cache access"
        # The higher the index in the base_access_ind list, the stronger the
        for access_ind in range(base_access_ind, len(access_list)):
            # Increment access to allow silent upgrades
            access = access_list[access_ind]

            # There
            for hl_cc_trace in self.high_level.cache.traces.start_state_dict[hl_cc_state]:
                if not hl_cc_trace.access:
                    continue

                if access == hl_cc_trace.access[0]:
                    ''' This is a redundant check if preselection of the ll_dir and hl_cache state based on access 
                    permission was performed in advance'''
                    # hl_access must not have less permissions in start state than ll_cache does
                    if not self.inclusive_relaxation:
                        ll_state_class = self.low_level.cache.state_classification[ll_access_trace.startstate]
                        hl_state_class = self.high_level.cache.state_classification[hl_cc_trace.startstate]

                        # Deactivated due to TSO-CC style protocols
                        if not ll_state_class <= hl_state_class:
                            continue

                    ''' Mandatory final state check'''
                    # Check the maximum ll cache access permissions associated with the ll directory state
                    ll_dir_state_class = self.low_level.dir_access_classification_map[ll_dir_trace.finalstate]

                    hl_state_class = self.high_level.cache.state_classification[hl_cc_trace.finalstate]

                    if not ll_dir_state_class <= hl_state_class:
                        self.ll_silent_upgrade_access(ll_access_trace, ll_dir_trace, hl_cc_trace)
                        hl_traces.append(hl_cc_trace)
                        continue

                    hl_traces.append(hl_cc_trace)

                    # additional safety check that once again verifies that the ll_cache_access <= hl_cache_access
                    assert self.low_level.cache.state_classification[ll_access_trace.finalstate] <= hl_state_class

                    new_cc_dir_tuple = CcDirStateTuple(ll_dir_trace, hl_cc_trace, None, ll_access_trace)
                    self._access_state_tuples[new_cc_dir_tuple] = new_cc_dir_tuple

            # For minimum access permission a match has been found, no upgrade required
            # Do not terminate in inner loop in case multiple transitions triggered by same access but different
            # guards exist
            if hl_traces:
                break

        assert hl_traces, "Fatal error no access traces found for higher level cache"
        return hl_traces

    # Check if lower level directory can be pre charged by conveying access permissions of external world to it
    def ll_silent_upgrade_access(self, ll_access_trace: Trace, ll_dir_trace: Trace, hl_cache_trace: Trace):

        # Get the high level directory traces and their maximum access permissions
        dir_traces: Dict[StateClassification, Trace] = {}

        for state_tuple in self.high_level.state_tuple_list:
            check_hl_access_trace = self.get_cache_access_trace(state_tuple, self.high_level)
            if hash(hl_cache_trace) == hash(check_hl_access_trace):
                hl_dir_trace = self.get_dir_trace(state_tuple, self.high_level)
                if not hl_dir_trace:
                    continue
                hl_dir_state_classification = self.high_level.dir_access_classification_map[hl_dir_trace.finalstate]
                dir_traces[hl_dir_state_classification] = hl_dir_trace

        if not dir_traces:
            return

        # Not more than one access assignment
        assert len(dir_traces) == 1, "Error unexpected number of remote trace state classifications"

        # Try to pre-charge the directory by performing access permissions remote cache might have
        proxy_access_tuple = self.ll_find_proxy_traces(list(dir_traces.values())[0],
                                                       ll_dir_trace.startstate)

        # Not more than one access assignment
        assert len(proxy_access_tuple) == 1, "Error unexpected number of remote trace state classifications"

        proxy_access_tuple = list(proxy_access_tuple.values())[0]

        first_proxy_trace = self.get_cache_access_trace(proxy_access_tuple, self.low_level)
        first_dir_trace = self.get_dir_trace(proxy_access_tuple, self.low_level)

        # Now get the access trace of the actual requesting cache
        for state_tuple in self.low_level.state_tuple_list:

            # Extract the directory trace
            second_dir_trace = self.get_dir_trace(state_tuple, self.low_level)

            if not second_dir_trace or second_dir_trace.startstate != first_dir_trace.finalstate:
                continue

            ll_access_trace = self.get_cache_access_trace(state_tuple, self.low_level)

            # If an access trace exists and the access trace contains load or store (not evict)
            if not ll_access_trace or ll_access_trace.access[0] != first_proxy_trace.access[0]:
                continue

            # Check if now the cache block is acquired with the same or weaker access permissions
            # Check the maximum ll cache access permissions associated with the ll directory state
            ll_dir_state_class = self.low_level.dir_access_classification_map[second_dir_trace.finalstate]
            hl_state_class = self.high_level.cache.state_classification[hl_cache_trace.finalstate]
            if not ll_dir_state_class <= hl_state_class:
                continue

            # System tuple found
            remote_trace = self.get_cache_remote_trace(state_tuple, self.low_level)

            if len(remote_trace) != 1:
                continue
            remote_trace = remote_trace[0]

            # Now only find the cache evict traces
            evict_trace_tuples = self._ll_extract_evict(remote_trace, second_dir_trace)

            for evict_trace_tuple in evict_trace_tuples:
                new_cc_dir_tuple = CcDirStateTuple(first_dir_trace + second_dir_trace + evict_trace_tuple[1],
                                            hl_cache_trace,
                                            first_proxy_trace + remote_trace + evict_trace_tuple[0],
                                            ll_access_trace)

                id_tuple = (first_dir_trace, second_dir_trace, evict_trace_tuple[1])
                self._silent_upgrade_state_tuples[id_tuple] = new_cc_dir_tuple

