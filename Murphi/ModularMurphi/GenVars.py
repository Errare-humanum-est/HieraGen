from typing import List

from DataObjects.ClassCluster import Cluster
from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler


class GenVars(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)

    def generate_vars(self, clusters: List[Cluster], verify_ssp=False):
        varstr = "--" + __name__ + self.nl
        varstr += "var " + self.nl

        archs = []
        for cluster in clusters:
            machines = set(cluster.system_tuple)
            for machine in machines:
                if machine.arch in archs:
                    continue
                archs.append(machine.arch)
                varstr += self._genMachines(machine.arch.get_unique_id_str())
        varstr += self.nl

        # TODO: This is a hack until a global network class is introduced
        parser = clusters[0].levels[0].parser
        varstr += self._gen_access_var() + self.nl
        varstr += self._genNetwork(parser.getNetwork()) + self.nl
        varstr += self._genFIFOs() + self.nl

        if verify_ssp:  # add extra bookkeeping for locking/unlocking
            varstr += self._gen_lock()

        return varstr

    def _genMachines(self, machine):
        varstr = ""
        varstr += self.tab + self.instsuf + machine + ": " + self.ObjKey + machine + self.end
        return varstr

    def _genNetwork(self, networks):
        varstr = ""
        for network in networks:
            definitions = network.getChildren()
            for definition in definitions:
                varstr += self._classNetwork(definition)

        return varstr

    def _classNetwork(self, definition):
        setup = definition.getChildren()
        if setup[0].getText() == self.ordered:
            return self._genOrderedNetwork(setup[1].getText())
        else:
            return self._genUnorderedNetwork(setup[1].getText())

    def _genOrderedNetwork(self, name):
        if name not in self.ONetworks:
            self.ONetworks.append(name)
        onet = self.tab + name + ": " + self.ObjKey + self.ordered + self.end
        onet += self.tab + self.countsuf + name + ": " + self.ObjKey + self.orderedcnt + self.end
        return onet

    def _genUnorderedNetwork(self, name):
        if name not in self.UNetworks:
            self.UNetworks.append(name)
        return self.tab + name + ": " + self.ObjKey + self.unordered + self.end

    def _genFIFOs(self):
        varstr = ""
        for network in self.ONetworks + self.UNetworks:
            varstr += self.tab + self.k_fifo + network + ": " + self.ObjKey + self.rfifo + self.end
        return varstr

    def _gen_lock(self):
        return self.tab + self.mutex + ": OBJ_LOCK" + self.end

    def _gen_access_var(self):
        return self.tab + self._openTemplate(self.faccesscheckvar) + self.nl
