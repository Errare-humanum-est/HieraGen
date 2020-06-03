from typing import List, Set

from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassCluster import Cluster

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler


class GenEnums(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)
        self.messageslist = []

    def gen_enum_str(self, clusters: List[Cluster]):
        typestr = "--" + __name__

        archs = []
        for cluster in clusters:
            machines = set(cluster.system_tuple)
            for machine in machines:
                if machine.arch not in archs:
                    archs.append(machine.arch)

        typestr += self.gen_stat_enum_str(archs)
        typestr += self.gen_dyn_enum_str(archs)
        return typestr

    def gen_stat_enum_str(self, archs: List[Architecture]):
        typestr = self.nl + "type" + self.nl

        # Access
        typestr += self.enumaccess(archs[0].parser.getAccess()) + self.nl

        # Implement more advance message detection in the future
        msg_str_list = []
        for arch in archs:
            msg_str_list += arch.get_message_name_str_list()

        # Messagetypes
        typestr += self.enummessages(set(msg_str_list))

        return typestr

    def enumaccess(self, accesses):
        retstr = self.kaccess + ": enum {" + self.nl + self.tab + "none"
        for access in accesses:
            retstr += "," + self.nl + self.tab + access
        retstr += self.nl + "};" + self.nl

        return retstr

    def enummessages(self, messages: Set[str]):
        sortmessages = sorted(list(messages))
        retstr = self.kmessages + ": enum { " + self.nl
        self.messageslist = sortmessages
        for ind in range(0, len(messages)-1):
            retstr += self.tab + sortmessages[ind] + "," + self.nl
        if sortmessages:
            retstr += self.tab + sortmessages[-1] + self.nl

        retstr += "};" + self.nl

        return retstr

    def gen_dyn_enum_str(self, archs: List[Architecture]):
        typestr = ""
        for arch in archs:
            typestr += self.enummachinestates(arch.get_states(), arch.get_unique_id_str(), self.statesuf) + self.nl
        return typestr

    def enummachinestates(self, machine, machinekey, suffix):
        retstr = ""

        retstr += self.nl + suffix + machinekey + ": enum { " + self.nl

        statekeys = sorted(machine.keys())

        for ind in range(0, len(statekeys) - 1):
            retstr += self.tab + machinekey + "_" + statekeys[ind] + "," + self.nl
        if statekeys:
            retstr += self.tab + machinekey + "_" + statekeys[-1] + self.nl

        retstr += "};" + self.nl

        return retstr
