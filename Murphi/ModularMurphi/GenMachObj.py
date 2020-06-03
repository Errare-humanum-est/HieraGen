from typing import List

from DataObjects.ClassMachine import Machine
from DataObjects.ClassCluster import Cluster
from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler

from Parser.ProtoCCcomTreeFct import *


class GenMachObj(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)
        self.GlobalInit = {}
        self.Vectordef = []
        self.maxdeferdepth = 1
        self.cluster_name: str = ""
        self.cluster_size: str = str(0)

    def gen_mach_obj_str(self, clusters: List[Cluster]):
        typestr = "--" + __name__ + self.nl

        defer = self.test_defer_clusters(clusters)

        if defer:
            typestr += self._typeBuffer() + self.nl

        archs = []

        for cluster in clusters:
            self.Vectordef = []
            machines = set(cluster.system_tuple)

            self.cluster_name = cluster.cluster_id + self.kmachines
            self.cluster_size = str(len(cluster.system_tuple))

            machstr = ""

            for machine in machines:
                if machine.arch in archs:
                    continue
                archs.append(machine.arch)
                machstr += self._gen_machine(machine.arch.get_data_object(), machine, defer) \
                           + self.nl
                machstr += self._genMultipleAddress(machine.arch.get_unique_id_str()) + self.nl
                machstr += self._genMachineObjects(machine.arch.get_unique_id_str()) + self.nl

            for entry in self.Vectordef:
                typestr += entry + self.nl

            typestr += machstr

        return typestr

    def _typeBuffer(self):
        return self._stringReplKeys(self._openTemplate(self.fbuffer),
                                    [self.maxdeferdepth, self.rmessage, self.rsendbuffer]
                                    ) + self.nl

    def _gen_machine(self, objects, machine: Machine, defer):
        objstr = ""

        machine_id = machine.arch.get_unique_id_str()

        init = {}
        objstr += self.EntryKey + machine_id + ": record" + self.nl

        objstr += self.tab + self.iState + ": " + self.statesuf + machine_id + self.end

        if defer:
            objstr += self.tab + self.iLL_Defer + ": " + self.rsendbuffer + self.end
            objstr += self.tab + self.iHL_Defer + ": " + self.rsendbuffer + self.end
            objstr += self.tab + self.iStall_Defer + ": " + self.rsendbuffer + self.end

        #objstr += self.tab + self.iAccess + ": " + self.kaccess + self.end

        defintions = objects[machine_id].getnode().getChildren()

        for inddef in range(0, len(defintions)):
            if not defintions[inddef].getText() in self.DataDef:
                continue
            method_fct = self.DataDef[defintions[inddef].getText()]
            method = getattr(self, method_fct, lambda: '_PassNode')
            res = method(defintions[inddef], init, machine_id)
            if res:
                for definition in res:
                    objstr += self.tab + definition + ": " + res[definition] + self.end

        objstr += "end" + self.end

        self.GlobalInit.update({machine_id: init})

        return objstr

    ####################################################################################################################
    # DATA TYPES
    ####################################################################################################################

    def _PassNode(self, definition, initial=0, machine=0):
        return 0

    def _genMultiset(self, definition, machname, refname):
        # It must be the global machine index to the current implementation of multicasts and Murphi restrictions
        machineset = self.kmachines

        vectorname = self.vectorsuf + machname + "_" + definition.getChildren()[0].getText() + "_" + machineset

        # Generic solution
        vector = vectorname + ": " + "multiset[" + self.cluster_size + "] of " + machineset + self.end

        vector += self.countsuf + vectorname + ": 0.." + self.cluster_size + self.end

        if vector not in self.Vectordef:
            self.Vectordef.append(vector)

        # Generic solution
        self.Vectormap.update({vectorname: machineset})

        if machname:
            self.Vectorassign.update({refname: {machineset: vectorname}})
            self.Vectorassign.update({machname: {machineset: vectorname}})

        return vectorname

    def _setInitState(self, definition, initial=0, machine=0):
        if isinstance(initial, dict):
            initial.update({self.iState: definition.getChildren()[0].getText()})
        else:
            return {definition.getText(): definition.getChildren()[0].getText()}
        return 0

    def _genData(self, definition, initial=0, machine=0):
        definitions = definition.getChildren()
        if len(definitions) > 1:
            settype = self._genMultiset(definitions[0], machine, definitions[-1].getText())
            return {definitions[-1].getText(): settype}
        else:
            if isinstance(initial, dict):
                initial.update({definitions[-1].getText(): "0"})
            return {definitions[-1].getText(): self.kcacheval}

    def _genID(self, definition, initial=0, machine=0):
        definitions = definition.getChildren()
        if len(definitions) > 1:
            settype = self._genMultiset(definitions[0], machine, definitions[-1].getText())
            return {definitions[-1].getText(): settype}
        else:
            return {definitions[-1].getText(): self.kmachines}

    def _genInt(self, definition, initial=0, machine=0):
        children = definition.getChildren()
        if len(children) > 2 and isinstance(initial, dict):
            initial.update({children[1].getText(): children[-1].getText()})

        outstr = ""
        rangedef = children[0].getChildren()
        for ind in range(1, len(rangedef) - 1):
            outstr += rangedef[ind].getText()

        return {children[1].getText(): outstr}

    def _genBool(self, definition, initial=0, machine=0):
        children = definition.getChildren()
        if len(children) > 2 and isinstance(initial, dict):
            initial.update({children[1].getText(): children[-1].getText()})
        else:
            initial.update({children[1].getText(): self.defval})

        return {children[1].getText(): "".join(childsToStringList(children[0]))}

    def _genMSG(self, definition, initial=0, machine=0):
        if isinstance(initial, dict):
            initial.update({definition.getChildren()[0].getText(): self.defval})
        return {definition.getChildren()[0].getText(): self.rmessage}

    ####################################################################################################################
    # MULTIPLE ADDRESS
    ####################################################################################################################

    def _genMultipleAddress(self, machine):
        objstr = ""
        objstr += self.MachKey + machine + ": record" + self.nl
        objstr += self.tab + self.CLIdent + ": array[" + self.kaddress + "] of " \
                  + self.EntryKey + machine + self.end
        objstr += "end" + self.end

        return objstr

    def _genMachineObjects(self, machine):
        objstr = ""

        objstr += self.ObjKey + machine +": array[" + self.SetKey + machine + "] of " + \
                 self.MachKey + machine + self.end

        return objstr
