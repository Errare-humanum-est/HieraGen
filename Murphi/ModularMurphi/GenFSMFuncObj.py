from antlr3.tree import CommonTree
import re
from typing import List, Dict
from Monitor.ClassDebug import Debug
from Parser.ProtoCCcomTreeFct import *

from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassMachine import Machine
from DataObjects.ClassCluster import Cluster
from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition

from Murphi.ModularMurphi.MurphiTokens import MurphiTokens
from Murphi.ModularMurphi.TemplateClass import TemplateHandler

from Parser.ForkTree import Node, ForkTree


class GenFSMFuncObj(MurphiTokens, TemplateHandler):

    def __init__(self, handler_dir: str):
        TemplateHandler.__init__(self, handler_dir)
        self.maxdeferdepth = 0
        self.func_local_var_names = [self.defmsgname]
        self.func_global_var_names = []

    def gen_arch_state_dict(self, clusters: List[Cluster]) -> Dict[str, Machine]:
        archs = {}
        for cluster in clusters:
            machines = set(cluster.system_tuple)
            for machine in machines:
                arch_name: str = machine.arch.get_unique_id_str()
                if arch_name not in archs:
                    archs[arch_name] = machine
        return archs

    def _generateObjFunc(self, clusters):
        behavstr = "--" + __name__ + self.nl
        archs = self.gen_arch_state_dict(clusters)

        # Generate non-access function
        for arch in sorted(archs.keys()):
            deferstr = ""

            if self.test_defer_arch(archs[arch].arch):
                deferstr += self._genDeferFunc(arch, MurphiTokens.iLL_Defer)
                deferstr += self._genDeferFunc(arch, MurphiTokens.iHL_Defer)
                deferstr += self._genDeferFunc(arch, MurphiTokens.iStall_Defer)

            archfuncstr = self._genArchNonAccessFunc(archs[arch])

            behavstr += deferstr + archfuncstr

        behavstr += self.nl + self.nl
        return behavstr

    def _genArchNonAccessFunc(self, machine: Machine):
        fctstr = self._genArchHeader(machine) + self.nl

        arch = machine.arch.get_unique_id_str()
        states = machine.arch.get_states()

        for state in sorted(states.keys()):
            fctstr += self._genArchState(arch, states[state]) + self.nl

        fctstr += self._genArchEnd() + self.nl

        return fctstr

    def _genArchState(self, arch, state: State):
        statestr = "case " + arch + "_" + state.getstatename() + ":" + self.nl
        statestr += "switch " + self.cinmsg + "." + self.cmtype + self.nl

        transitions = state.getdataack() + state.getremote() + \
                      [trans for trans in state.getaccess() if trans.getinmsg()]

        guard_list = []
        for transition in transitions:
            guard_list.append(transition.getguard())
        guard_list = list(set(guard_list))

        transitions.sort(key=lambda transition: (transition.getguard(),
                                                 transition.getcond(),
                                                 transition.getfinalstate().getstatename()))

        op_string = ""
        for guard in guard_list:
            guard_trans = [transition for transition in transitions if transition.getguard() == guard]
            op_string += self.gen_operation_str(arch, guard_trans)

        statestr += self._addtabs(op_string, 1)

        statestr += self.tab + " else return false" + self.end
        statestr += "endswitch" + self.end

        return self._addtabs(statestr, 1)

    def gen_operation_str(self, arch: str, transitions: List[Transition]) -> str:
        return self.convert_operation_tree(self.gen_operation_tree(arch, transitions)) + self.nl

    def gen_single_trans_operation_str(self, arch: str, transitions: List[Transition]) -> str:
        return self.convert_operation_tree_wo_case(self.gen_operation_tree(arch, transitions)) + self.nl

    def gen_operation_tree(self, arch: str, transitions: List[Transition]) -> ForkTree:
        # Make the root node
        operation_tree = ForkTree()

        check_guard = []
        for transition in transitions:
            check_guard.append(transition.getguard())
        assert len(set(check_guard)) == 1, "Transitions to create operation tree from have different guards"

        # Node data is a tuple (operation object, operation string)
        guard = check_guard.pop()
        base_node = operation_tree.insertnode((guard, "case " + guard + ":" + self.nl))

        for transition in transitions:
            # Reset tree to base node
            operation_tree.set_cur_node(base_node)
            for operation in transition.operation:
                # Get children
                access_str = self.process_operation(operation, arch, transition)

                if not self.tree_find_children(access_str, operation_tree):
                    operation_tree.insertnode((operation, access_str))

            # After last operation insert final state
            final_state_str = self._genFinalState(arch, transition)
            if not self.tree_find_children(final_state_str, operation_tree):
                operation_tree.insertnode((final_state_str, final_state_str))

            # Set access permission
            access_permission_str = self._genArchAccess(transition)
            if not self.tree_find_children(access_permission_str, operation_tree):
                operation_tree.insertnode((access_permission_str, access_permission_str))

        return operation_tree

    def tree_find_children(self, operation_str: str, operation_tree: ForkTree) -> bool:
        cur_children = operation_tree.get_direct_children()
        for child_node in cur_children:
            node_str = child_node.getdata()[1]
            if node_str == operation_str:
                # Found output string as children, select children to be next
                operation_tree.set_cur_node(child_node)
                return True
        return False

    def check_operation_tree(self, operation_tree: ForkTree):
        # Check for each node, whether not more than one operation assignment exists
        for node in operation_tree.get_nodes():
            cnt = 0
            for child in node.getsuccessors():
                # The data is a tuple(operation, operation_string)
                if child.getdata()[0].getText() == self.tCOND and child.getdata()[0].getText() == self.tNCOND:
                    cnt += 1
            assert cnt <= 1, "More than one children found that is not a condition"
        pass

    def convert_operation_tree(self, operation_tree: ForkTree) -> str:
        # At the last child nodes print return true at the end!
        base_node = operation_tree.get_base_node()
        return base_node.getdata()[1] + self._addtabs(self.tree_node_to_string(base_node), 1)

    def convert_operation_tree_wo_case(self, operation_tree: ForkTree) -> str:
        # At the last child nodes print return true at the end!
        base_node = operation_tree.get_base_node()
        return self._addtabs(self.tree_node_to_string(base_node), 1)

    def tree_node_to_string(self, node: Node) -> str:
        op_string = ""

        children = node.getsuccessors()
        if not children:
            return op_string

        children = self.sort_nodes_cond(children)
        # Track the first if, then every other cond is elif and the only non cond is else
        first = 0
        for child in children:

            child_operation = child.getdata()[0]
            if isinstance(child_operation, CommonTree):
                child_operation = child_operation.getText()

            if child_operation == self.tCOND or child_operation == self.tNCOND:
                if not first:
                    op_string += self.kif + child.getdata()[1]
                    first = 1
                    # Parse children and add them with an additional formatting tab
                    op_string += self._addtabs(self.tree_node_to_string(child), 1)
                else:
                    op_string += self.kelsif + child.getdata()[1]
                    op_string += self._addtabs(self.tree_node_to_string(child), 1)

            else:
                # Non if instruction
                    if first:   # There exists an if condition tree
                        op_string += self.kelse + self.nl

                    op_string += child.getdata()[1]
                    op_string += self.tree_node_to_string(child)

        if first:  # There exists an if condition tree
            op_string += self.kendif + self.end

        return op_string

    def sort_nodes_cond(self, nodes: List[Node]):
        cond_nodes = []
        other_nodes = []
        for node in nodes:

            node_operation = node.getdata()[0]
            if isinstance(node_operation, CommonTree):
                node_operation = node_operation.getText()

            if node_operation == self.tCOND or node_operation == self.tNCOND:
                cond_nodes.append(node)
            else:
                other_nodes.append(node)

        return cond_nodes + other_nodes

    def process_operation(self, operation: CommonTree, arch: str, transition: Transition):
        inmsgtype = transition.getrefguard() if transition.getrefguard() else transition.getguard()

        if operation.getText() == self.tASSIGN:
            return self._genArchAssignment(operation, arch, inmsgtype, transition)

        if operation.getText() == self.tMODSTATEFUNC:
            return self._gen_mod_state_func(operation, arch) + self.end

        if operation.getChildren()[0].getText() == self.iState:
            return self._genArchAccess(transition)

        if operation.getText() == self.tSEND:
            return self._genSendFunction(operation) + self.end

        if operation.getText() == self.tMCAST:
            return self._genMCastFunction(operation) + self.end

        if operation.getText() == self.tBCAST:
            return self._genBCastFunction(operation) + self.end

        # For every if cond=true, there exists an else (if cond=false)
        if operation.getText() == self.tCOND:
            return self._genIfCondFunction(operation, 0, arch, inmsgtype) + self.nl

        if operation.getText() == self.tNCOND:
            return self._genIfCondFunction(operation, 1, arch, inmsgtype) + self.nl

        if operation.getText() == self.tSETFUNC:
            return self._genSetFunction(operation, arch, inmsgtype) + self.end

        # DEFER FUNCTION FUNCTIONALITY
        if operation.getText() == self.tPUSH_HL_DEFER:
            msg_name =  str(operation.children[1])
            if msg_name in self.messageslist:
                msg_name = self.cinmsg
            return self._genmsgDeferpush(arch, msg_name, MurphiTokens.iHL_Defer)

        if operation.getText() == self.tPUSH_LL_DEFER:
            msg_name =  str(operation.children[1])
            if msg_name in self.messageslist:
                msg_name = self.cinmsg
            return self._genmsgDeferpush(arch, msg_name, MurphiTokens.iLL_Defer)

        if operation.getText() == self.tPUSH_STALL_DEFER:
            msg_name =  str(operation.children[1])
            if msg_name in self.messageslist:
                msg_name = self.cinmsg
            return self._genmsgDeferpush(arch, msg_name, MurphiTokens.iStall_Defer)

    ####################################################################################################################
    # DeferMsgs
    ####################################################################################################################

    def _genDeferFunc(self, arch: str, defer_type: str):
        return self._stringReplKeys(self._openTemplate(self.fbufferfunc),
                                    [self.instsuf + arch,
                                     self.kmachines,
                                     self.maxdeferdepth,
                                     self.rmessage,
                                     defer_type]
                                    ) + self.nl

    def _genmsgDeferpush(self, arch: str, msg_name: str, defer_type: str):
        return self._stringReplKeys(self._openTemplate(self.fdeferpushfunc),
                                    [self.instsuf + arch, defer_type, msg_name, self.cadr, self.cmach]
                                    ) + self.nl

    def _genmsgDeferpop(self, arch: str, defer_type: str):
        return self._stringReplKeys(self._openTemplate(self.fdeferpopfunc),
                                    [self.instsuf + arch, defer_type, self.cadr, self.cmach]
                                    ) + self.nl

    ####################################################################################################################
    # VARIABLE ASSIGNMENT
    ####################################################################################################################

    def _genArchAssignment(self, operation, arch, inmsgtype, transition):
        statestr = ""
        tokens = operation.getChildren()
        varname = tokens[0].getText()
        if tokens[-1].getText() == self.tMSGCSTR:
            statestr += varname + " := "
            statestr += self._genMessageAssignment(arch, inmsgtype, tokens[-1])
            statestr += self.end

        elif tokens[-1].getText() == self.tSEND_BASE_DEFER:
            if tokens[-1].children[0].text == self.rmessage:
                statestr += varname + " := " + self.iHL_Defer + "_"
                statestr += self._genMessageAssignment(arch, inmsgtype, tokens[-1])
            else:
                statestr += varname + " := " + self.iHL_Defer + "_"
                statestr += self._genMessageAssignmentBase(arch, inmsgtype, tokens[-1])
            statestr += self.end

        elif tokens[-1].getText() == self.tPOP_HL_DEFER:
            statestr += varname + " := " + self._genmsgDeferpop(arch, MurphiTokens.iHL_Defer)
        elif tokens[-1].getText() == self.tPOP_LL_DEFER:
            statestr += varname + " := " + self._genmsgDeferpop(arch, MurphiTokens.iLL_Defer)
        elif tokens[-1].getText() == self.tPOP_STALL_DEFER:
            statestr += varname + " := " + self._genmsgDeferpop(arch, MurphiTokens.iStall_Defer)

        else:
            statestr += self._resolveVarNames(varname) + " := "
            if tokens[0].getText() == self.iState:
                statestr += arch + "_" + transition.getfinalstate().getstatename() + self.end
            elif tokens[-1].getText() == self.tSETFUNC:
                statestr += self._genSetFunction(tokens[-1], arch, inmsgtype) + self.end
            else:
                for ind in range(2, len(tokens)):
                    statestr += self._resolveChildren(tokens[ind])
                statestr += self.end

        return statestr

    ####################################################################################################################
    # FINAL STATE AND ACCESS PERMISSION ASSIGNMENT
    ####################################################################################################################

    def _genFinalState(self, arch: str, transition: Transition):
        return self.ccle + "." + self.iState + " := " + arch + "_" + \
               transition.getfinalstate().getstatename() + self.end

    def _genArchAccess(self, transition):
        access = transition.getfinalstate().getaccesshit()

        guards = [guard.getguard() for guard in access]

        accesstype = self.defaccess

        if len(access):
            for memaccess in self.memaccessdef:
                if memaccess in guards:
                    accesstype = memaccess

        if accesstype == self.defaccess:
            return "Clear_acc(" + self.cadr + ", " + self.cmach + ")" + self.end
        elif accesstype == self.defstore:
            return "Set_store(" + self.cadr + ", " + self.cmach + ")" + self.end
        elif accesstype == self.defload:
            return "Set_load(" + self.cadr + ", " + self.cmach + ")" + self.end
        else:
            assert 0, "Unknown access"

    ####################################################################################################################
    # ARCH HEADER
    ####################################################################################################################

    def _genArchHeader(self, machine: Machine):
        arch = machine.arch.get_unique_id_str()
        fctheader = "function Func_" + arch + \
                    "(" + self.cinmsg + ":" + self.rmessage + "; " + self.cmach + ":" + self.SetKey + arch \
                    + ") : boolean" + self.end

        all_var_name_dict = self._get_variable_names(machine.arch)
        global_var_name_dict = machine.arch.data_object.variables
        local_var_names_dict = self._filter_local_variables(all_var_name_dict, global_var_name_dict)
        self.func_local_var_names = list(local_var_names_dict.keys())
        self.func_global_var_names = list(global_var_name_dict.keys())
        fctheader += self._gen_local_variables(local_var_names_dict)

        fctheader += "begin" + self.nl
        fctheader += self.tab + "alias " + self.cadr + ": " + self.cinmsg + "." + self.cadr + " do" + self.nl
        fctheader += self.tab + "alias " + self.ccle + \
                     ": " + self.instsuf + arch + "[" + self.cmach + "]." + self.CLIdent + "[" + self.cadr + "] do" \
                     + self.nl
        fctheader += "switch " + self.ccle + "." + self.iState + self.nl

        return fctheader

    def _get_variable_names(self, arch: Architecture) -> Dict[str, str]:
        var_names_type = {}
        for transition in arch.transitions:
            for operation in transition.operation:
                if str(operation) == self.tASSIGN:
                    if str(operation.children[0]) not in var_names_type:
                        var_names_type[str(operation.children[0])] = str(operation.children[2])
        return var_names_type

    def _filter_local_variables(self, all_var_names_type: Dict[str, str],
                                global_var_name_dict: Dict[str, str]) -> Dict[str, str]:
        local_var_names = {}
        for var_name in all_var_names_type:
            if var_name not in global_var_name_dict:
                local_var_names[var_name] = all_var_names_type[var_name]
        return local_var_names

    def _gen_local_variables(self, local_var_name_dict: Dict[str, str]):
        var_str = ""
        for var_name in local_var_name_dict:
            type_str = ""
            if local_var_name_dict[var_name] == self.tMSGCSTR:
                type_str = self.rmessage
            elif (local_var_name_dict[var_name] == self.tSEND_BASE_DEFER or
                  local_var_name_dict[var_name] == self.tPOP_HL_DEFER or
                  local_var_name_dict[var_name] == self.tPOP_LL_DEFER or
                  local_var_name_dict[var_name] == self.tPOP_STALL_DEFER):
                type_str = self.rmessage
            else:
                assert 0, "Unknown message type"
            var_str += "var " + var_name + ": " + type_str + self.end
        return var_str

    def _genArchEnd(self):
        fctfooter = "endswitch" + self.end
        endalias = "endalias" + self.end
        endalias += "endalias" + self.end
        fctfooter += self._addtabs(endalias, 1) + self.nl
        fctfooter += "return true" + self.end
        fctfooter += "end" + self.end
        return fctfooter

    ####################################################################################################################
    # SET FUNCTION
    ####################################################################################################################

    def _genSetFunction(self, objects, arch, guard):
        objectstr = ''.join(childsToStringList(objects))
        param = re.search("\((.*)\)", objectstr).group(1)
        func = re.sub("\((.*)\)", "", objectstr)
        split = func.rsplit('.', 1)

        param1 = self._resolveMsgScrDest(split[0], arch, guard)
        param2 = self._resolveMsgScrDest(param, arch, guard)

        method_fct = self.SetFuncDef[split[1]]
        method = getattr(self, method_fct, lambda: '_PassNode')
        #if split[0] not in self.Vectorassign:
        #    return "DEBUG"
        return method(list(self.Vectorassign[split[0]].values())[0], param1, param2)

    @staticmethod
    def _genVectAdd(vectortype, param1, param2):
        return "AddElement_" + vectortype + "(" + param1 + "," + param2 + ")"

    @staticmethod
    def _genVectDel(vectortype, param1, param2):
        return "RemoveElement_" + vectortype + "(" + param1 + "," + param2 + ")"

    @staticmethod
    def _genVectClear(vectortype, param1, param2):
        return "ClearVector_" + vectortype + "(" + param1 + ")"

    @staticmethod
    def _genVectCont(vectortype, param1, param2):
        return "IsElement_" + vectortype + "(" + param1 + "," + param2 + ")"

    @staticmethod
    def _genVectEmpty(vectortype, param1, param2):
        return "HasElement_" + vectortype + "(" + param1 + "," + param2 + ")"

    @staticmethod
    def _genVectCnt(vectortype, param1, param2):
        return "VectorCount_" + vectortype + "(" + param1 + ")"

    ####################################################################################################################
    # SET FUNCTION
    ####################################################################################################################
    def _gen_mod_state_func(self, operation: CommonTree, arch: str):
        return "ModifyStates_" + arch + "(" + self.cmach + ", " \
               + arch + "_" + str(operation.children[0]) + ", " \
               + arch + "_" + str(operation.children[1]) + ")"

    ####################################################################################################################
    # SEND FUNCTION
    ####################################################################################################################
    def _genSendFunction(self, objects):
        objectstr = ""
        # Check transition defer messages
        definitions = objects.getChildren()

        network = definitions[0].getText()
        msgname = definitions[1].getText()

        # Does not need to be deferred
        objectstr += "Send_" + network + "(" + msgname + ")"

        return objectstr

    def _genMCastFunction(self, objects):
        objectstr = ""
        # Check transition defer messages
        definitions = objects.getChildren()

        network = definitions[0].getText()
        msgname = definitions[1].getText()
        vectorname = definitions[2].getText()

        # Does not need to be deferred
        objectstr += "Multicast_" + network + "_" + list(self.Vectorassign[vectorname].values())[0] + \
                     "(" + msgname + "," + self.ccle + "." + vectorname + ")"
        return objectstr

    def _genBCastFunction(self, objects):
        objectstr = ""
        # Check transition defer messages
        definitions = objects.getChildren()

        network = definitions[0].getText()
        msgname = definitions[1].getText()

        # Does not need to be deferred
        objectstr += "Broadcast_" + network + "(" + msgname + ")"
        return objectstr

    @staticmethod
    def _msgCompare(msg1, msg2):
        ref1 = msg1 if isinstance(msg1, str) else msg1.getmsgtype()
        ref2 = msg2 if isinstance(msg2, str) else msg2.getmsgtype()

        if ref1 == ref2:
            return True
        return False

    ####################################################################################################################
    # COND FUNCTION
    ####################################################################################################################
    def _genIfCondFunction(self, objects, negation, arch, inmsgtype):
        definitions = objects.getChildren()

        outstr = ""

        if negation:
            outstr += "!"

        outstr += "("

        for definition in definitions:
            sel = definition.getText()
            if sel == self.tSETFUNC:
                outstr += self._genSetFunction(definition, arch, inmsgtype)

            elif sel in self.Opmap:
                outstr += self.Opmap[sel]

            else:
                outstr += self._resolveVarNames(''.join(toStringList(definition)))

        outstr += ") then"

        return outstr

    def _genElseCondFunction(self):
        return "else"

    ####################################################################################################################
    # MESSAGE ASSIGNMENT
    ####################################################################################################################

    def _genMessageAssignmentBase(self, arch, message, objects):
        definition = objects.getChildren()
        msgobj = definition[0].getText()
        msgtype = definition[1].getText()

        # Request(adr: Address; mtype: MessageType; src: Machines; dst: Machines;

        conststr = msgobj + "(" + definition[1].getText()

        if len(definition) > 2:
            for ind in range(2, len(definition)):
                if definition[ind].getText() == self.tSETFUNC:
                    conststr += "," + self._genSetFunction(definition[ind], arch, message)
                else:
                    conststr += "," + self._resolveChildren(definition[ind])

        conststr += ")"

        return conststr

    def _genMessageAssignment(self, arch, message, objects):
        definition = objects.getChildren()
        msgobj = definition[0].getText()

        msgtype = definition[1].getText()

        msgsrc = self._resolveMsgScrDest("".join(toStringList(definition[2])), arch, message)
        msgdst = self._resolveMsgScrDest("".join(toStringList(definition[3])), arch, message)

        # Request(adr: Address; mtype: MessageType; src: Machines; dst: Machines;

        conststr = msgobj + "("
        # Address
        conststr += self.cadr + ","
        # Messagetype
        conststr += msgtype + ","
        conststr += msgsrc + ","
        conststr += msgdst

        if len(definition) > 4:
            for ind in range(4, len(definition)):
                if definition[ind].getText() == self.tSETFUNC:
                    conststr += "," + self._genSetFunction(definition[ind], arch, message)
                else:
                    conststr += "," + self._resolveChildren(definition[ind])

        conststr += ")"

        return conststr

    def _resolveChildren(self, definition):
        if isinstance(definition, str):
            objectstr = definition
        elif definition.getChildren():
            objectstr = ''.join(toStringList(definition))
        else:
            objectstr = definition.getText()
        return self._resolveVarNames(objectstr)

    def _resolveMsgScrDest(self, objectstr: str, arch, guard: str):
        split = objectstr.split('.', 1)

        if len(split) > 1:
            if split[0] == guard:
                return self.cinmsg + '.' + split[1]
            elif split[0] in self.messageslist:
                self.pdebugwarning("Message substituted: " + guard)
                return self.cinmsg + '.' + split[1]
            elif split[0] in self.func_local_var_names:
                return '.'.join(split)
            else:
                return split[0]
        if split[0] == self.iID:
            return self.cmach
        else:
            return self.ccle + '.' + split[0]

    def _resolveVarNames(self, objectstr):
        split = objectstr.split('.', 1)

        if split[0] in self.messageslist:
            del split[0]
            return self.cinmsg + '.' + ''.join(split)
        elif split[0] in self.func_local_var_names:
            return '.'.join(split)
        elif split[0] in self.func_global_var_names:
            return self.ccle + '.' + ''.join(split)
        elif split[0] in self.constant_list:
            return split[0]
        else:
            if len(split) == 1:
                if split[0] == self.iID:
                    return self.cmach
                elif self._testInt(split[0]) or not split[0].isalpha():
                    return split[0]
            return self.ccle + '.' + ''.join(split)

