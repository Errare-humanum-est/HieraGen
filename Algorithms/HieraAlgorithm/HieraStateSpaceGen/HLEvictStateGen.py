from typing import List, Tuple, Dict

from DataObjects.ClassState import State
from DataObjects.ClassLevel import Level
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple

from Algorithms.HieraAlgorithm.HieraStateSpaceGen.StateTupleBaseFunc import StateTupleBaseFunc


class HLEvictStateGen(StateTupleBaseFunc):
    def __init__(self, low_level: Level, high_level: Level):
        StateTupleBaseFunc.__init__(self)
        self.low_level = low_level
        self.high_level = high_level

    """
    ####################################################################################################################
    ##### evict implementation HL
    ####################################################################################################################
    """
    # We utilize the knowledge, that in any protocol writes need to be linearized
    # So if the higher level cache does an eviction, the lower level proxy cache needs to perform a write
    # This is necessary, because in the future, after the eviction remote caches might acquire and modify the cache line
    # All lower level caches handled by the evicting dir/cache controller must be made aware of this
    def hl_evict_traces(self, state_sets: List[Tuple[State, State]]) -> List[CcDirStateTuple]:
        cc_dir_tuples: Dict[CcDirStateTuple, CcDirStateTuple] = {}
        for state_set in state_sets:
            cc_state = state_set[1]
            for hl_cc_trace in self.high_level.cache.traces.start_state_dict[cc_state]:
                # If it is an evict transaction
                if hl_cc_trace.access == self.high_level.cache.init_state.evict:
                    ll_state_class = self.low_level.dir_access_classification_map[state_set[0]]
                    hl_state_class = self.high_level.cache.state_classification[hl_cc_trace.finalstate]
                    if ll_state_class <= hl_state_class:
                        new_cc_dir_tuple = CcDirStateTuple(state_set[0], hl_cc_trace)
                        cc_dir_tuples[new_cc_dir_tuple] = new_cc_dir_tuple

        return list(cc_dir_tuples.values())
