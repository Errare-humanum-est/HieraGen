from Algorithms.HieraAlgorithm.HieraStateTupleClass.ControllerMappings import *
from DataObjects.ClassLevel import Level
from DataObjects.ClassState import State
from Algorithms.HieraAlgorithm.HieraStateTupleClass.CcDirStateTuple import CcDirStateTuple

from Algorithms.HieraAlgorithm.HieraStateSpaceGen.LLAccessStateGen import LLAccessStateGen
from Algorithms.HieraAlgorithm.HieraStateSpaceGen.HLRemoteStateGen import HLRemoteStateGen
from Algorithms.HieraAlgorithm.HieraStateSpaceGen.LLEvictStateGen import LLEvictStateGen
from Algorithms.HieraAlgorithm.HieraStateSpaceGen.HLEvictStateGen import HLEvictStateGen


class HieraStateSpaceGen(LLAccessStateGen, HLRemoteStateGen, LLEvictStateGen, HLEvictStateGen):
    def __init__(self, low_level: Level, high_level: Level):

        LLAccessStateGen.__init__(self, low_level, high_level)
        HLRemoteStateGen.__init__(self, low_level, high_level)
        LLEvictStateGen.__init__(self, low_level, high_level)
        HLEvictStateGen.__init__(self, low_level, high_level)

        self.low_level = low_level
        self.high_level = high_level

        self.low_level_cache_dict: Dict[State] = {}

        '''
        pessimistic_access: If true and lower level has silent upgrades, the higher level must have acquired 
        the cache line with the required immediate access permissions. 
        '''
        self.pessimistic_access = False
        print("PESSIMISTIC MODE: " + str(self.pessimistic_access))



        # Handle all ll accesses at directory and find matching high level traces
        self.stable_state_state_tuples = self.state_space_generation()
        # Handle ll accesses
        self.access_traces_top_down(self.stable_state_state_tuples)
        #self.access_state_tuples: List[CcDirStateTuple] = self.access_traces_top_down(self.stable_state_state_tuples)
        # Handle remote accesses
        self.remote_state_tuples: List[CcDirStateTuple] = self.remote_traces(self.stable_state_state_tuples)
        # Handle ll evict
        self.ll_evict_state_tuples: List[CcDirStateTuple] = self.ll_evict_traces(self.stable_state_state_tuples)
        # Handle hl evict
        self.hl_evict_state_tuples: List[CcDirStateTuple] = self.hl_evict_traces(self.stable_state_state_tuples)

    """
    ####################################################################################################################
    ##### State space generation
    ####################################################################################################################
    """

    # CcDir controller state space generation
    def state_space_generation(self):
        state_sets = []

        init_state = (self.low_level.directory.init_state, self.high_level.cache.init_state)
        state_sets.append(init_state)

        for ll_dir_state in self.low_level.dir_access_classification_map:
            ll_cc_state_class = self.low_level.dir_access_classification_map[ll_dir_state]
            for hl_cc_state in self.high_level.cache.stable_states:
                if ll_cc_state_class <= self.high_level.cache.state_classification[hl_cc_state]:
                    new_conv_state = (ll_dir_state, hl_cc_state)
                    if new_conv_state not in state_sets:
                        state_sets.append(new_conv_state)

        return list(set(state_sets))

    #def sort_state_tuples_startstate