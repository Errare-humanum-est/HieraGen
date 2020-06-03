from typing import List

from DataObjects.ClassCluster import Cluster

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler


class GenAccessFunc(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)

    def gen_access_func(self, clusters: List[Cluster]):
        machines = []
        for cluster in clusters:
            for machine in cluster.system_tuple:
                if machine not in machines:
                    machines.append(machine)

        access_type = "--" + __name__ + self.nl
        access_type += self._stringReplKeys(self._openTemplate(self.faccesscheckfunc),
                                            [self.kaddress, self.kmachines]) + self.nl + self.nl
        return access_type
