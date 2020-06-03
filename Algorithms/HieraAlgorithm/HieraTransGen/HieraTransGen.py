from typing import List, Dict

from DataObjects.ClassState import State
from DataObjects.ClassLevel import Level

from Algorithms.HieraAlgorithm.HieraTransGen.LLAccessTransGen import LLAccessTransGen
from Algorithms.HieraAlgorithm.HieraTransGen.LLUpgradeTransGen import LLUpgradeTransGen
from Algorithms.HieraAlgorithm.HieraTransGen.HLRemoteTransGen import HLRemoteTransGen
from Algorithms.HieraAlgorithm.HieraTransGen.LLEvictTransGen import LLEvictTransGen
from Algorithms.HieraAlgorithm.HieraTransGen.HLEvictTransGen import HLEvictTransGen


class HieraTransGen(LLAccessTransGen, LLUpgradeTransGen, HLRemoteTransGen, LLEvictTransGen, HLEvictTransGen):
    def __init__(self, low_level: Level, high_level: Level):

        LLAccessTransGen.__init__(self, low_level, high_level)
        LLUpgradeTransGen.__init__(self, low_level, high_level)
        HLRemoteTransGen.__init__(self, low_level, high_level)
        LLEvictTransGen.__init__(self)
        HLEvictTransGen.__init__(self)

        self.cc_dir_to_cc_state_map: Dict[State, List[State]] = {}
        self.cc_dir_to_dir_state_map: Dict[State, List[State]] = {}
