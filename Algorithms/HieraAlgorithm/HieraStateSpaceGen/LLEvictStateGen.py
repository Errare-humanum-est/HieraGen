from typing import List, Tuple, Dict

from DataObjects.ClassState import State
from DataObjects.ClassLevel import Level
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple

from Algorithms.HieraAlgorithm.HieraStateSpaceGen.StateTupleBaseFunc import StateTupleBaseFunc


class LLEvictStateGen(StateTupleBaseFunc):
    def __init__(self, low_level: Level, high_level: Level):
        StateTupleBaseFunc.__init__(self)
        self.low_level = low_level
        self.high_level = high_level

        '''
        pessimistic_access: If true and lower level has silent upgrades, upon eviction the higher level must issue a 
        store in the higher level cache to perform an upgrade        
        '''
        self.pessimistic_access = False

        self._ll_evict_state_tuples: Dict[CcDirStateTuple, CcDirStateTuple] = {}
        self._ll_evict_upgrade_state_tuples: Dict[CcDirStateTuple, CcDirStateTuple] = {}

        self.ll_evict_state_tuples: List[CcDirStateTuple] = []
        self.ll_evict_upgrade_state_tuples: List[CcDirStateTuple] = []
    """
    ####################################################################################################################
    ##### evict request implementation LL
    ####################################################################################################################
    """

    def ll_evict_traces(self, state_sets: List[Tuple[State, State]]) -> List[CcDirStateTuple]:
        self._ll_evict_state_tuples: Dict[CcDirStateTuple, CcDirStateTuple] = {}

        # First generate all the non-concurrent state transaction
        for state_set in state_sets:
            dir_state = state_set[0]
            hl_state = state_set[1]

            for state_tuple in self.low_level.state_tuple_list:
                ll_dir_trace = self.get_dir_trace(state_tuple, self.low_level)
                if not ll_dir_trace or not ll_dir_trace.startstate == dir_state:
                    continue

                ll_cc_trace = self.get_cache_access_trace(state_tuple, self.low_level)
                if not ll_cc_trace or not ll_cc_trace.access[0] in self.low_level.cache.init_state.evict:
                    continue

                # Add the handling of the Exclusive state here....

                new_cc_dir_tuple = \
                    CcDirStateTuple(ll_dir_trace, state_set[1], None, state_tuple.get_arch_access_trace())
                self._ll_evict_state_tuples[new_cc_dir_tuple] = new_cc_dir_tuple

        # Now generate all concurrent state transactions, if a transaction
        concurrent_cc_dir_tuples: Dict[CcDirStateTuple, CcDirStateTuple] = {}
        for state in self.low_level.cache.stable_states:

            # Find the cache evict traces
            cc_evict_traces = []
            for evict_trace in self.low_level.cache.traces.start_state_dict[state]:
                for evict_access in evict_trace.access:
                    if evict_access in self.low_level.cache.init_state.evict:
                        cc_evict_traces.append(evict_trace)

            if not cc_evict_traces:
                continue

            # For every ll_cache and directory combination all remaining accesses must be added
            for state_set in state_sets:
                dir_state = state_set[0]

                dir_state_traces = self.low_level.directory.traces.start_state_dict[dir_state]

                # Check if the complementary evict trace exists in the directory
                for cc_evict_trace in cc_evict_traces:
                    for dir_state_trace in dir_state_traces:
                        if set(cc_evict_trace.outmsg).intersection(set(dir_state_trace.inmsg)):
                            new_cc_dir_tuple = \
                                CcDirStateTuple(dir_state_trace, state_set[1], None, cc_evict_trace)
                            concurrent_cc_dir_tuples[new_cc_dir_tuple] = new_cc_dir_tuple

                    # If for the current cache state eviction trace not complementary directory eviction trace was found
                    # then throw an error
                    #assert found, "Forbidden behaviour"

        # Update the eviction dictionary
        self._ll_evict_state_tuples.update(concurrent_cc_dir_tuples)
        return list(self._ll_evict_state_tuples.values())
