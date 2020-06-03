from typing import List
from Parser.ProtoCCcomTreeFct import *
from DataObjects.ClassCluster import Cluster
from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler


class GenNetworkObj(MurphiTokens, TemplateHandler):
    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)
        self.BaseMsg = [self.madr, self.mtype, self.msrc, self.mdst]
        self.SuperMsg = []

    def gen_network_str(self, clusters: List[Cluster], cfifomax: int = 0):
        obj_str = "--" + __name__ + self.nl

        # Child inherits from GlobalVariables that supplies this function
        #if self.test_defer_clusters(clusters):
            #obj_str += self._genMessageHeader()
        obj_str += self._genMessage(clusters)
        obj_str += self._typeFIFO(cfifomax) + self.nl
        obj_str += self._genNetworkObjects()
        obj_str += self._genFIFOObjects()

        return obj_str + self.nl

    '''
    # BASE MESSAGE DEFERRING DISABLED
    def _genMessageHeader(self):
        objstr = self.rbasemessage + ": record" + self.nl

        for defpair in self.BaseMsg:
            for definition in defpair:
                objstr += self.tab + definition + ": " + defpair[definition] + self.end

        objstr += "end" + self.end + self.nl
        return objstr
    '''

    def _genMessage(self, clusters: List[Cluster]):

        objects = []
        for cluster in clusters:
            for level in cluster.levels:
                if level not in objects:
                    objects += level.message_objects

        typedefs = {}
        objstr = self.rmessage + ": record" + self.nl

        for defpair in self.BaseMsg:
            for definition in defpair:
                objstr += self.tab + definition + ": " + defpair[definition] + self.end

        for obj in objects:
            defintions = obj.getnode().getChildren()

            for inddef in range(1, len(defintions)):
                if not defintions[inddef].getText() == self.SetKey:

                    definition = toStringList(defintions[inddef])
                    if self.Initval in definition:
                        typedefs.update({definition[definition.index(self.Initval) - 1]: defintions[inddef]})
                    else:
                        typedefs.update({definition[-1]: defintions[inddef]})

        for typekey in sorted(typedefs.keys()):
            method_fct = self.DataDef[typedefs[typekey].getText()]
            method = getattr(self, method_fct, lambda: '_PassNode')
            res = method(typedefs[typekey])

            if res:
                if res not in self.SuperMsg:
                    self.SuperMsg.append(res)
                for definition in res:
                    objstr += self.tab + definition + ": " + res[definition] + self.end

        objstr += "end" + self.end

        return objstr

    def _typeFIFO(self, cfifomax: int):
        return self._stringReplKeys(self._openTemplate(self.ffifo),
                                    [str(cfifomax)]
                                    ) + self.nl

    def _genNetworkObjects(self):
        objstr = ""
        # Ordered Interconnect
        objstr += self.ObjKey + self.ordered + ": array[" + self.kmachines + \
                  "] of array[0.." + self.cordered + "-1] of " + self.rmessage + self.end
        objstr += self.ObjKey + self.orderedcnt + ": array[" + self.kmachines + \
                  "] of 0.." + self.cordered + self.end
        objstr += self.ObjKey + self.unordered + ": array[" + self.kmachines + \
                  "] of multiset[" + self.cunordered + "] of " + self.rmessage + self.end

        return objstr

    def _genFIFOObjects(self):
        return self.ObjKey + self.rfifo + ": array[" + self.kmachines + "] of " + self.rfifo + self.end
