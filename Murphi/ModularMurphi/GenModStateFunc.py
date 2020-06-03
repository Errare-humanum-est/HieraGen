from typing import List, Dict

from DataObjects.ClassCluster import Cluster

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler
from DataObjects.ClassMachine import Machine


class GenModStateFunc(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)

    def gen_mod_state_func(self, clusters: List[Cluster]):
        mod_state_func = "--" + __name__ + self.nl

        machine_dict: Dict[str, Machine] = {}
        for cluster in clusters:
            for machine in cluster.system_tuple:
                if machine.arch.get_unique_id_str() not in machine_dict:
                    machine_dict[machine.arch.get_unique_id_str()] = machine

        for machine in machine_dict.values():
            mod_state_func += self._stringReplKeys(self._openTemplate(self.fmodifystate),
                                                   [machine.arch.get_unique_id_str(), self.kmachines,
                                                    self.statesuf, self.instsuf, self.iState]) + self.nl

        return mod_state_func + self.nl
