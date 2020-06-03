from typing import List, Dict
from DataObjects.ClassState import State
from DataObjects.ClassMachine import Machine
from DataObjects.ClassCluster import Cluster
from DataObjects.ClassTransition import Transition
from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler
from DataObjects.ClassMultiDict import MultiDict


class GenAccessRuleset(MurphiTokens, TemplateHandler):
    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)

    def gen_access_rules(self, clusters: List[Cluster], verify_ssp=False):
        behavstr = "--" + __name__ + self.nl        # Generate access function\

        for cluster in clusters:
            machines = set(cluster.system_tuple)
            for machine in machines:
                access_str = self.generate_arch_access_func(machine, verify_ssp)
                if verify_ssp and access_str:
                    access_str += self._generateUnlockRules(machine)
                behavstr += access_str

        return behavstr

    def generate_arch_access_func(self, machine: Machine, verify_ssp):
        states: Dict[str, State] = machine.arch.get_states()
        rulesetstr = ""

        for state in sorted(states.keys()):
            if [trans for trans in states[state].getaccess() if trans.getaccess() and not trans.getinmsg()] \
                      + states[state].getevictmiss():
                break
            return rulesetstr

        rulesetstr = self._genAccessHeader(machine.arch.get_unique_id_str()) + self.nl

        rulestr = ""
        for state in sorted(states.keys()):
            if len(states[state].getaccessmiss() + states[state].getevictmiss()):
                rulestr += self._genAccessState(machine.arch.get_unique_id_str(), states[state], verify_ssp) \
                           + self.nl

        rulesetstr += self._addtabs(rulestr, 1)

        rulesetstr += self._genAccessEnd() + self.nl

        return rulesetstr

    def _genAccessHeader(self, arch):
        fctstr = "ruleset " + self.cmach + ":" + self.SetKey + arch + " do" \
                 + self.nl
        fctstr += "ruleset " + self.cadr + ":" + self.kaddress + " do" + self.nl
        fctstr += self.tab + "alias " + self.ccle + ":" + self.instsuf + arch \
                  + "[" + self.cmach + "]." + self.CLIdent + "[" + self.cadr \
                  + "] do" + self.nl

        return fctstr

    def _genAccessEnd(self):
        statestr = self.tab + "endalias" + self.end
        statestr += "endruleset" + self.end
        statestr += "endruleset" + self.end

        return statestr

    def _genAccessState(self, arch, state: State, verify_ssp: bool=False):
        transitions = [trans for trans in state.getaccess() if trans.getaccess() and not trans.getinmsg()] \
                      + state.getevictmiss()

        trans_dict = MultiDict()

        for transition in transitions:
            trans_dict[transition.getguard()] = transition

        statestr = ""

        for guard in trans_dict:

            ruleid = arch + "_" + str(state) + "_" + guard

            ccle_dot_state = self.ccle + "." + self.iState

            statestr += "rule \"" + ruleid + "\"" + self.nl
            statestr += self.tab + ccle_dot_state + " = " + arch + "_" + str(state) + self.nl

            statestr += self.gen_network_ready_test(trans_dict[guard])

            # Add network ready check here

            if verify_ssp:
                statestr += " & " + self._LockTest() + self.nl
            statestr += "==>" + self.nl
            if verify_ssp:
                statestr += self._LockAcquire() + self.end
            statestr += self.tab + self.tSEND + ruleid + "(" + self.cadr + ", m)" + self.end
            statestr += "endrule" + self.end + self.nl

        return statestr

    def _generateUnlockRules(self, machine: Machine):
        mach_name = machine.arch.get_unique_id_str()
        rulesetstr = self._genAccessHeader(mach_name)
        rulestr = ""

        for state in machine.arch.get_stable_states():
            ruleid = self.mutex + " " + mach_name + "_" + str(state)
            rulestr += "rule \"" + ruleid + "\"" + self.nl
            rulestr += self.tab + self.ccle + "." + self.iState + " = " + mach_name + "_" + str(state)
            rulestr += " & " + self._LockRelease()
            rulestr += "==>" + self.nl
            rulestr += "endrule" + self.end + self.nl

        rulesetstr += self._addtabs(rulestr, 1)
        rulesetstr += self._genAccessEnd() + self.nl

        return rulesetstr

    def _LockTest(self):
        return "LockTest()"

    def _LockAcquire(self):
        return "LockAcquire(" + self.cmach + ")"

    def _LockRelease(self):
        return "LockRelease(" + self.cmach + ")"

    def gen_network_ready_test(self, transitions: List[Transition]):
        network_ready_cond = ""

        vc_list = []
        for transition in transitions:
            for outmsg in transition.outMsg:
                vc_list.append(str(outmsg.vc))

        for vc in set(vc_list):
            network_ready_cond += " & " + str(vc) + self.tnetworkready

        if network_ready_cond:
            network_ready_cond += self.nl
        return network_ready_cond
