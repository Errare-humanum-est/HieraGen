from typing import List
from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassCluster import Cluster
from Murphi.ModularMurphi.MurphiTokens import MurphiTokens


class GlobalVariables(MurphiTokens):

    def __init__(self):
        self.kmachnames: List[str] = []

    def test_defer_clusters(self, clusters: List[Cluster]):
        for cluster in clusters:
            machines = set(cluster.system_tuple)
            for machine in machines:
                if self.test_defer_arch(machine.arch):
                    return True
        return False

    def test_defer_arch(self, arch: Architecture) -> bool:
        return arch.test_token(self.tPUSH_HL_DEFER) or \
               arch.test_token(self.tPUSH_LL_DEFER) or \
               arch.test_token(self.tPUSH_STALL_DEFER)
