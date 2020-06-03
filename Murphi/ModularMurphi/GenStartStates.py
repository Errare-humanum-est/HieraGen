from typing import List

from DataObjects.ClassCluster import Cluster
from DataObjects.ClassMachine import Machine
from DataObjects.ClassArchitecture import Architecture

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler


class GenStartStates(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)
        self.ONetworks = []
        self.UNetworks = []
        self.GlobalInit = []
        self.BaseMsg = [self.madr, self.mtype, self.msrc, self.mdst]
        self.SuperMsg = []

    def generate_start_state(self, clusters: List[Cluster], verify_ssp=False):
        startstr = "--" + __name__ + self.nl
        startstr += "startstate" + self.nl + self.nl

        startdef = self._gen_reset_body(clusters)

        if verify_ssp:
            startdef += self._gen_lock_reset()

        startstr += self._addtabs(startdef, 1)
        startstr += self.nl + "endstartstate" + self.end
        return startstr

    def _gen_reset_body(self, clusters: List[Cluster]):
        startdef = ""
        filtered_machines = []

        for cluster in clusters:
            machines = set(cluster.system_tuple)
            for machine in machines:
                if machine not in filtered_machines:
                    filtered_machines.append(machine)

        for machine in filtered_machines:
            startdef += self._genMachineInit(machine.arch)

        startdef += self._genFIFOInit()
        startdef += self._genNetworkInit() + self.nl
        startdef += self._genAccessReset() + self.nl
        return startdef

    def _genMachineInit(self, arch: Architecture):
        mach_name = arch.get_unique_id_str()

        dirstr = self._genInitObjectHeader(mach_name)
        dirprefix = self.instsuf + mach_name + "[i]." + self.CLIdent + "[a]."
        dirstr += self._addtabs(self._genObjectInit(dirprefix, arch, self.GlobalInit[mach_name]), 1)
        dirstr += self._genInitObjectEnd() + self.nl
        return dirstr

    def _genInitObjectHeader(self, objname):
        header = "for i:" + self.SetKey + objname + " do" + self.nl
        header += "for a:" + self.kaddress + " do" + self.nl
        return header

    def _genInitObjectEnd(self):
        return "endfor" + self.end + "endfor" + self.end

    def _genObjectInit(self, prefix, arch: Architecture, definitions):
        startstr = ""
        for definition in sorted(definitions):
            if definition == self.iState:
                startstr += prefix + definition + " := " + arch.get_unique_id_str() + "_" + \
                            str(arch.init_state) + self.end
            else:
                startstr += prefix + definition + " := " + definitions[definition] + self.end

        if self.test_defer_arch(arch):
            startstr += prefix + self.iLL_Defer + ".QueueInd := 0" + self.end
            startstr += prefix + self.iHL_Defer + ".QueueInd := 0" + self.end
            startstr += prefix + self.iStall_Defer + ".QueueInd := 0" + self.end

        return startstr

    def _genFIFOInit(self):
        startstr = ""
        for network in self.ONetworks + self.UNetworks:
            inputstr = self._openTemplate(self.ffifoinit)
            replacekeys = [self.k_fifo + network]

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            startstr += inputstr + self.nl

        return startstr

    def _genNetworkInit(self):
        startstr = self._genUnorderedNetInit()
        startstr += self._genOrderedNetInit()

        return startstr

    def _genUnorderedNetInit(self):
        startstr = ""
        for network in self.UNetworks:
            startstr += self._stringReplKeys(self._openTemplate(self.funorderedinit), [network]) + self.nl

        return startstr

    def _genOrderedNetInit(self):
        startstr = ""
        for network in self.ONetworks:
            startstr += self._stringReplKeys(self._openTemplate(self.forderedinit),
                                             [network, self.countsuf + network]
                                             ) + self.nl

        return startstr


    def _genAccessReset(self):
        return "Reset_acc()" + self.end


    def _gen_lock_reset(self):
        return "LockReset()" + self.end + self.nl
