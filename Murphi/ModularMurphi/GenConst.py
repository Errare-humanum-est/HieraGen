from typing import List

from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassCluster import Cluster

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler


class GenConst(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)
        self.constant_list = []

    def gen_const_str(self, clusters: List[Cluster],
                        enableFIFO,
                        cvalmax,
                        cadrcnt,
                        corderedsz,
                        cunorderedsz
                        ):
        conststr = "--" + __name__ + self.nl
        conststr += self.gen_static_const_str(enableFIFO, cvalmax, cadrcnt, corderedsz, cunorderedsz)

        archs = []
        for cluster in clusters:
            machines = set(cluster.system_tuple)
            for machine in machines:
                if machine.arch not in archs:
                    archs.append(machine.arch)

        conststr += self.gen_dyn_const_str(archs)

        return conststr

    def gen_static_const_str(self,
                             enableFIFO,
                             cvalmax,
                             cadrcnt,
                             corderedsz,
                             cunorderedsz
                             ):

        conststr = self._stringReplKeys(self._openTemplate(self.fconst),
                                        ["true" if enableFIFO else "false"]
                                        )

        conststr += self.tab + self.cvalcntid + ": " + str(cvalmax) + self.end
        conststr += self.tab + self.cadrcntid + ": " + str(cadrcnt) + self.end
        conststr += self.nl
        conststr += self.tab + self.cordered + ": " + str(corderedsz) + self.end
        conststr += self.tab + self.cunordered + ": " + str(cunorderedsz) + self.end
        conststr += self.nl

        return conststr

    def gen_dyn_const_str(self, archs: List[Architecture]):
        global_const_dict = {}
        for arch in archs:
            global_const_dict.update(arch.get_constants())

        conststr = ""
        for const_def in global_const_dict:
            self.constant_list.append(const_def)
            conststr += self.tab + const_def + ": " + global_const_dict[const_def] + self.end

        return conststr
