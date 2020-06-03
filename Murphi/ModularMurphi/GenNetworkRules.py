from typing import List, Tuple

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler
from DataObjects.ClassCluster import Cluster


class GenNetworkRules(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)
        self.ONetworks = []
        self.UNetworks = []

    ####################################################################################################################
    # FIFO RECEIVE RULE
    ####################################################################################################################
    def gen_fifo_rule(self, clusters: List[Cluster]):

        rulestr = "--" + __name__ + self.nl

        for network in self.ONetworks + self.UNetworks:
            archs = self.get_machines(clusters)
            cond_rule_str = self.gen_cond_rule_part(self.gen_if_elif_structure(archs),
                                                    self.ffiforuleinner,
                                                    [self.k_fifo + network])

            cond_rule_str = self._addtabs(cond_rule_str, 4)
            inputstr = self._openTemplate(self.ffiforule)
            replacekeys = [self.k_fifo + network, cond_rule_str]

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            rulestr += inputstr + self.nl

        return rulestr

    ####################################################################################################################
    # NETWORK RECEIVE RULES
    ####################################################################################################################
    def gen_network_rules(self, clusters: List[Cluster]):
        rulestr = self._genUnorderedNetRule(clusters)
        rulestr += self._genOrderedNetRule(clusters)

        return rulestr

    def _genUnorderedNetRule(self, clusters: List[Cluster]):
        rulestr = ""
        for network in self.UNetworks:
            archs = self.get_machines(clusters)
            cond_rule_str = self.gen_cond_rule_part(self.gen_if_elif_structure(archs),
                                                    self.funorderedruleinner)
            cond_rule_str = self._addtabs(cond_rule_str, 4)

            inputstr = self._openTemplate(self.funorderedrule)
            replacekeys = [network, self.k_fifo + network, cond_rule_str]

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            rulestr += inputstr + self.nl

        return rulestr

    def _genOrderedNetRule(self, clusters: List[Cluster]):
        rulestr = ""
        for network in self.ONetworks:
            archs = self.get_machines(clusters)
            cond_rule_str = self.gen_cond_rule_part(self.gen_if_elif_structure(archs),
                                                    self.forderedruleinner,
                                                    [network])

            cond_rule_str = self._addtabs(cond_rule_str, 4)
            inputstr = self._openTemplate(self.forderedrule)
            replacekeys = [network, self.countsuf + network, self.k_fifo + network, cond_rule_str]

            for ind in range(0, len(replacekeys)):
                inputstr = self._stringRepl(inputstr, ind, replacekeys[ind])

            rulestr += inputstr + self.nl

        return rulestr

    def get_machines(self, clusters: List[Cluster]) -> List[str]:
        archs = []
        for cluster in clusters:
            machines = set(cluster.system_tuple)
            for machine in machines:
                arch_name = machine.arch.get_unique_id_str()
                if arch_name not in archs:
                    archs.append(arch_name)
        return archs

    def gen_if_elif_structure(self, archs: List[str]) -> List[Tuple[str, str]]:
        cond = []
        for ind in range(0, len(archs)):
            if ind == 0:
                cond.append(('if', archs[ind]))
            else:
                cond.append(('elsif', archs[ind]))
            if ind == len(archs)-1:
                cond.append(('else', None))
        return cond

    def gen_cond_rule_part(self, cond_archs: List[Tuple[str, str]], rule_file: str, list_id: List[str] = None):
        cond_str = ""
        for cond_arch in cond_archs:
            cond_str += cond_arch[0]
            if cond_arch[1]:
                cond_str += " IsMember(n, " + self.SetKey + cond_arch[1] + ") then" + self.nl
                if list_id:
                    str_list = list_id + [cond_arch[1]]
                else:
                    str_list = [cond_arch[1]]
                cond_str += self._stringReplKeys(self._openTemplate(rule_file), str_list) + self.nl
            else:
                cond_str += ' error \"unknown machine\"' + self.end
        cond_str += 'endif' + self.end + self.nl
        return cond_str

