from typing import List, Dict

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler

from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassCluster import Cluster
from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition
from DataObjects.ClassMultiDict import MultiDict


class GenAccessSendFunc(MurphiTokens, TemplateHandler):
    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)
        self.func_local_var_names = [self.defmsgname]
        self.func_global_var_names = []

    def _gen_arch_access_send_func(self, clusters: List[Cluster]):
        sendfctstr = "--" + __name__ + self.nl
        archs = self.get_machines_dict(clusters)
        for arch in archs:
            sendfctstr += self.gen_access_send_func(archs[arch])

        return sendfctstr

    def gen_access_send_func(self, arch: Architecture):
        sendfctstr = ""

        states = arch.get_states()

        for state in states:
            if [trans for trans in states[state].getaccess() if trans.getaccess() and not trans.getinmsg()] \
                      + states[state].getevictmiss():
                break
            return sendfctstr

        for state in sorted(states.keys()):
            if len(states[state].getaccessmiss() + states[state].getevictmiss()):
                sendfctstr += self._genAccessSendFunc(arch, states[state]) + self.nl

        return sendfctstr

    def _genAccessSendFunc(self, arch: Architecture, state: State):
        transitions = [trans for trans in state.getaccess() if trans.getaccess() and not trans.getinmsg()] \
                      + state.getevictmiss()

        trans_dict = MultiDict()

        for transition in transitions:
            trans_dict[transition.getguard()] = transition

        sendfctstr = ""

        for guard in trans_dict:
            ruleid = arch.get_unique_id_str() + "_" + str(state) + "_" + guard

            sendfctstr += self._genSendFunctionHeader(arch, ruleid, trans_dict[guard]) + self.nl

        return sendfctstr

    def _genSendFunctionHeader(self, arch: Architecture, ruleid, transitions: List[Transition]):
        arch_id = arch.get_unique_id_str()
        fctstr = "procedure " + self.tSEND + ruleid + \
                    "(" + self.cadr + ":" + self.kaddress + "; m:" + self.SetKey + arch_id + ")" + self.end

        all_var_name_dict = self._get_variable_names(arch)
        global_var_name_dict = arch.data_object.variables
        local_var_names_dict = self._filter_local_variables(all_var_name_dict, global_var_name_dict)
        self.func_local_var_names = list(local_var_names_dict.keys())
        self.func_global_var_names = list(global_var_name_dict.keys())
        fctstr += self._gen_local_variables(local_var_names_dict)

        fctstr += "begin" + self.nl
        fctstr += self.tab + "alias " + self.ccle + ": " + self.instsuf \
                  + arch_id + "[" + self.cmach + "]." + self.CLIdent \
                  + "[" + self.cadr + "] do" + self.nl
        fctstr += self.gen_single_trans_operation_str(arch_id, transitions)
        fctstr += "endalias" + self.end
        fctstr += "end" + self.end + self.nl

        return fctstr

    def get_machines_dict(self, clusters: List[Cluster]) -> Dict[str, Architecture]:
        archs = {}
        for cluster in clusters:
            machines = set(cluster.system_tuple)
            for machine in machines:
                arch_name = machine.arch.get_unique_id_str()
                if arch_name not in archs:
                    archs[arch_name] = machine.arch
        return archs
