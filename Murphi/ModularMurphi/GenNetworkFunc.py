from typing import List, Dict
from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler
from DataObjects.ClassCluster import Cluster

from Algorithms.NetworkAnalysis.ClassNetwork import ClassNetwork


class GenNetworkFunc(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)
        self.ONetworks = []
        self.UNetworks = []
        self.BaseMsg = [self.madr, self.mtype, self.msrc, self.mdst]
        self.SuperMsg = []

    def gen_network_func(self, clusters: List[Cluster], cfifomax):
        funcstr = "--" + __name__

        # Fifo functions
        funcstr += self._stringReplKeys(self._openTemplate(self.ffifofunc),
                                        [str(cfifomax)]
                                        ) + self.nl

        # Ordered Networks Send
        funcstr += self._genordsendFunc() + self.nl

        # Unordered Networks Send
        funcstr += self._genunordsendFunc() + self.nl
        funcstr += self._genMulticastFunc() + self.nl
        funcstr += self._genBroadcastFunc() + self.nl
        funcstr += self._genVectorFunc() + self.nl

        # Add generate network ready ordered and unordered detection
        funcstr += self._gen_network_ready(clusters) + self.nl

        # Generate Message Constructors
        funcstr += self._genMessageConstr(clusters)

        if self.test_defer_clusters(clusters):
            pass
            # NO BASE MESSAGE DEFERRING
            #funcstr += self._genBaseMessageConstr()
            #funcstr += self._genMessageConstrBase(clusters)

        return funcstr

    '''
    ####################################################################################################################
    GENERAL MESSAGE AND NETWORK FUNCTIONALITY
    ####################################################################################################################
    '''
    def _genMessageConstr(self, clusters: List[Cluster]):
        objects = []
        for cluster in clusters:
            for level in cluster.levels:
                objects += level.message_objects

        objects = list(set(objects))

        constrstr = ""

        for obj in objects:
            objname = obj.getname()
            items = []

            constr = "function " + objname + "("

            for defpair in self.BaseMsg:
                for definition in defpair:
                    constr += definition + ": " + defpair[definition] + "; "
                    items.append(definition)

            defintions = obj.getnode().getChildren()
            for inddef in range(1, len(defintions)):
                definition = defintions[inddef].getChildren()[-1].getText()
                for defpair in self.SuperMsg:
                    if definition in defpair:
                        constr += definition + ": " + defpair[definition] + "; "
                        items.append(definition)

            constr = constr.rsplit(';', 1)[0]
            constr += ") : " + self.rmessage + self.end
            constr += "var " + self.defmsgname + ": " + self.rmessage + self.end
            constr += "begin" + self.nl

            for defpair in self.BaseMsg:
                for definition in defpair:
                    constr += self.tab + self.defmsgname + "." + definition + " := " + definition + self.end

            for defpair in self.SuperMsg:
                for definition in defpair:
                    if definition in items:
                        constr += self.tab + self.defmsgname + "." + definition + " := " + definition + self.end
                    else:
                        constr += self.tab + self.defmsgname + "." + definition + " := " + self.defval + self.end

            constr += self.tab + "return " + self.defmsgname + self.end
            constr += "end" + self.end

            constrstr += constr + self.nl

        return constrstr

    def _genordsendFunc(self):
        sendfunc = ""
        for network in self.ONetworks:
            replacekeys = [network, self.countsuf + network, self.cordered]
            inputstr = self._openTemplate(self.fonetwork)

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            sendfunc += inputstr + self.nl

        return sendfunc

    def _genunordsendFunc(self):
        sendfunc = ""
        for network in self.UNetworks:
            replacekeys = [network, self.cunordered]
            inputstr = self._openTemplate(self.funetwork)

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            sendfunc += inputstr + self.nl

        return sendfunc

    def _genMulticastFunc(self):
        sendfunc = ""
        for network in self.ONetworks + self.UNetworks:
            for vector in self.Vectormap:
                replacekeys = [network, vector]
                inputstr = self._openTemplate(self.fmulticast)

                for ind in range(0, len(replacekeys)):
                    inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

                sendfunc += inputstr + self.nl

        return sendfunc

    def _genBroadcastFunc(self):
        sendfunc = ""
        for network in self.ONetworks + self.UNetworks:
            replacekeys = [network]
            inputstr = self._openTemplate(self.fbroadcast)

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            sendfunc += inputstr + self.nl

        return sendfunc

    def _genVectorFunc(self):
        vecfunc = ""

        for vector in self.Vectormap:
            replacekeys = [vector, self.Vectormap[vector], self.countsuf + vector]
            inputstr = self._openTemplate(self.fvector)

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            vecfunc += inputstr + self.nl

        return vecfunc

    '''
    ####################################################################################################################
    BASE MESSAGE FUNCTIONALITY
    ####################################################################################################################
    '''
    def _genBaseMessageConstr(self):
        constr = "function " + self.iHL_Defer + "_" + self.rbasemessage + "("
        items = []

        for defpair in self.BaseMsg:
            for definition in defpair:
                constr += definition + ": " + defpair[definition] + "; "
                items.append(definition)

        constr += ") : " + self.rbasemessage + self.end
        constr += "var " + self.defmsgname + ": " + self.rbasemessage + self.end
        constr += "begin" + self.nl

        for defpair in self.BaseMsg:
            for definition in defpair:
                constr += self.tab + self.defmsgname + "." + definition + " := " + definition + self.end

        constr += self.tab + "return " + self.defmsgname + self.end
        constr += "end" + self.end

        constr += self.nl

        return constr

    def _genMessageConstrBase(self, clusters: List[Cluster]):
        objects = []
        for cluster in clusters:
            for level in cluster.levels:
                objects += level.message_objects

        objects = list(set(objects))

        constrstr = ""

        for obj in objects:
            objname = obj.getname()
            items = []

            constr = "function " + self.iHL_Defer + "_" + objname + "("

            constr += self.cbasemsg + ": " + self.rbasemessage + "; "

            defintions = obj.getnode().getChildren()
            for inddef in range(1, len(defintions)):
                definition = defintions[inddef].getChildren()[-1].getText()
                for defpair in self.SuperMsg:
                    if definition in defpair:
                        constr += definition + ": " + defpair[definition] + "; "
                        items.append(definition)

            constr = constr.rsplit(';', 1)[0]
            constr += ") : " + self.rmessage + self.end
            constr += "var " + self.defmsgname + ": " + self.rmessage + self.end
            constr += "begin" + self.nl

            for defpair in self.BaseMsg:
                for definition in defpair:
                    constr += self.tab + self.defmsgname + "." + definition + " := " + \
                              self.cbasemsg + "." + definition + self.end

            for defpair in self.SuperMsg:
                for definition in defpair:
                    if definition in items:
                        constr += self.tab + self.defmsgname + "." + definition + " := " + definition + self.end
                    else:
                        constr += self.tab + self.defmsgname + "." + definition + " := " + self.defval + self.end

            constr += self.tab + "return " + self.defmsgname + self.end
            constr += "end" + self.end

            constrstr += constr + self.nl

        return constrstr

    def _gen_network_ready(self, clusters: List[Cluster]) -> str:
        message_bound = 1       # Depends on the maximum number of requests that are issued by a single cache
        networks: Dict[str, ClassNetwork] = {}
        constrstr = ""
        for cluster in clusters:
            for level in cluster.levels:
                request_networks = level.network_class.req_networks
                for request_network in request_networks:
                    network_spec = level.network_class.networks[request_network]
                    networks[request_network] = network_spec

        constrstr += self.gen_onetwork_ready(networks, message_bound)
        constrstr += self.gen_unetwork_ready(networks, message_bound)

        return constrstr

    def gen_onetwork_ready(self, networks: Dict[str, ClassNetwork], msg_bound=1) -> str:
        onetwork_ready_str = ""
        for network in networks:
            network_spec = networks[network]
            if network_spec.network_type == network_spec.ordered:
                onetwork_ready_str += self._stringReplKeys(self._openTemplate(self.fonetworkready),
                                                           [network, self.countsuf, self.cordered, str(msg_bound)]
                                                           ) + self.nl
        return onetwork_ready_str

    def gen_unetwork_ready(self, networks: Dict[str, ClassNetwork], msg_bound=1) -> str:
        unetwork_ready_str = ""
        for network in networks:
            network_spec = networks[network]
            if network_spec.network_type == network_spec.unordered:
                unetwork_ready_str += self._stringReplKeys(self._openTemplate(self.funetworkready),
                                                           [network, self.cunordered, str(msg_bound)]
                                                           ) + self.nl
        return unetwork_ready_str
