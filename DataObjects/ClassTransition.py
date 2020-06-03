from antlr3.tree import CommonTree
from typing import List, Dict, Union

import copy

from DataObjects.ClassMessage import Message
from DataObjects.ClassStateNode import StateNode

from Algorithms.General.AuxStateHandler import AuxStateHandler

from DataObjects.ClassTransClassification import TransitionClassificationEnum


class Transition:
    def __init__(self, startstate, finalstate, access='', inmsg='', outmsg='', cond='', operation=''):

        if access:
            assert isinstance(access, str) or isinstance(access, Message)

        if not startstate.testaccess(access) and inmsg == '':
            self.inMsg: str = access
            self.access: str = ''
        else:
            self.access: str = access
            self.inMsg: str = inmsg

        if inmsg:
            assert isinstance(inmsg, Message)

        if isinstance(outmsg, list) and all(isinstance(msg, Message) for msg in outmsg):
            self.outMsg: List[Message] = outmsg
        elif isinstance(outmsg, Message):
            self.outMsg: List[Message] = [outmsg]
        elif outmsg == '':
            self.outMsg: List[Message] = []
        else:
            assert 0, "Unknown output message format"

        if operation:
            if isinstance(operation, list):
                assert all(isinstance(entry, CommonTree) for entry in operation)
                self.operation: List[CommonTree] = operation
            else:
                assert isinstance(operation, CommonTree)
                self.operation: List[CommonTree] = [operation]
        else:
            self.operation: List[CommonTree] = []

        # The cond field is used by ProtoGen do determine whether concurrency was already introduced to a state,
        # by comparing transition guards and conditions
        # The operation field is vital for the correctness of the parser
        if cond:
            if isinstance(cond, list):
                assert all(isinstance(entry, str) for entry in cond)
                self.cond: List[str] = cond
            else:
                assert isinstance(cond, CommonTree)
                self.cond = [cond]
        else:
            self.cond = []

        self.comm_class = None
        self.access_class = TransitionClassificationEnum.invalid    # UNUSED
        self.startState = startstate
        self.finalState = finalstate

        # The defermsg contains the name of the deferred messages and the deferred operations actually contain
        # the operations that need to be performed
        self.defermsg = []
        self.deferred_operations = []

        self.refguard = ''
        self.outmsgrename = {}
        self.inmsgrename = {}

    def __str__(self):
        return str(self.startState) + " -- " + str(self.inMsg) + str(self.access) + " -> " + str(self.finalState)

    def get_hash(self):
        return hash((str(self.startState), str(self.finalState), str(self.access), str(self.inMsg),
                     str([str(operation) for operation in self.operation])))

    def get_hash_ignore_finale_state(self):
        return hash((str(self.startState), str(self.access), str(self.inMsg),
                     str([str(operation) for operation in self.operation])))

########################################################################################################################
# SETUP FUNCTIONS
########################################################################################################################
    def addoperation(self, treenode):
        assert isinstance(treenode, CommonTree)
        self.operation.append(treenode)

    def add_operation_list(self, operations: List[CommonTree]):
        self.operation += operations

    def getoperation(self):
        return self.operation

    def setstartstate(self, startstate: Union[StateNode, 'State']):
        self.startState = startstate

    def getstartstate(self):
        return self.startState

    def setfinalstate(self, finalstate: Union[StateNode, 'State']):
        self.finalState = finalstate

    def getfinalstate(self):
        return self.finalState

    def getaccess(self) -> str:
        return self.access

    def getinmsg(self) -> str:
        return self.inMsg

    def setinmsg(self, inmsg: Message):
        assert isinstance(inmsg, Message)
        self.inMsg = inmsg

    def addoutmsg(self, message: Message):
        assert isinstance(message, Message)
        self.outMsg.append(message)

    def getoutmsg(self) -> List[Message]:
        return self.outMsg

    def add_out_msg_list(self, out_msg: Union[Message, List[Message]]):
        if isinstance(out_msg, List):
            self.outMsg += out_msg
        else:
            assert isinstance(out_msg, Message)
            self.outMsg += [out_msg]

    def deferoutmsg(self, defermsgs=0) -> List[str]:
        if not defermsgs:
            msg = self.outMsg
            self.outMsg = []
            self.defermsg += [entry for entry in msg if entry not in self.defermsg]
            return msg

        else:
            newoutmsg = []
            defermsg = []
            for msg in self.outMsg:
                if isinstance(msg, Message):
                    msgid = msg.getmsgtype()
                else:
                    msgid = msg
                if msgid in defermsgs:
                    defermsg.append(msg)
                else:
                    newoutmsg.append(msg)

            self.defermsg += [entry for entry in defermsg if entry not in self.defermsg]
            self.outMsg = newoutmsg

            return defermsg

    def set_out_msg(self, out_msg_list: List['State']):
        self.outMsg = out_msg_list

    def getdefermsg(self):
        return self.defermsg

    def getguard(self):
        if self.inMsg:
            if isinstance(self.inMsg, Message):
                guard = self.inMsg.getmsgtype()
            else:
                guard = self.inMsg
        else:
            guard = self.access

        #if self.access:
        #    guard = self.access
        #else:
        #    if isinstance(self.inMsg, Message):
        #        guard = self.inMsg.getmsgtype()
        #    else:
        #        guard = self.inMsg
        return guard

    def getrefguard(self):
        return self.refguard

    def addcond(self, cond):
        self.cond.append(cond)

    def getcond(self):
        return self.cond

    def getoutmsgrenamed(self):
        return self.outmsgrename

    def getoutmsgtypes(self):
        msgouttypes = []
        for message in self.outMsg:
            if isinstance(message, str):
                msgouttypes.append(message)
            else:
                msgouttypes.append(message.getmsgtype())
        return msgouttypes

    def rename_inmsg_operation(self, msg_name: str, new_msg_name: str):
        if msg_name == str(self.inMsg):
            self.inmsgrename[msg_name] = new_msg_name
            self.rename_in_msg(msg_name, new_msg_name)
            # update all message tokens
            self.rename_operation(msg_name, new_msg_name)

    def rename_outmsg_operation(self, msg_name: str, new_msg_name: str):
        self.outmsgrename[msg_name] = new_msg_name
        self.rename_out_msg(msg_name, new_msg_name)
        # update all message tokens
        self.rename_operation(msg_name, new_msg_name)

    def rename_operation(self, cur_var: str, new_var: str):
        self.operation = AuxStateHandler.cond_operations_var_rename(self.operation, cur_var, new_var)

    def rename_in_msg(self, msg_name: str, new_msg_name: str):
        if isinstance(self.inMsg, Message):
            self.inMsg.type = new_msg_name
        else:
            self.inMsg = new_msg_name

    def rename_out_msg(self, msg_name: str, new_msg_name: str):
        for outMsg in self.outMsg:
            if str(outMsg) == msg_name:
                outMsg.type = new_msg_name

    ####################################################################################################################
    # COMMON
    ####################################################################################################################

    def copy_modify_trans(self, startstate: 'State', finalstate: 'State'):
        newtrans = copy.copy(self)
        newtrans.setstartstate(startstate)
        newtrans.setfinalstate(finalstate)
        return newtrans

    def deepcopy_modify_trans_except_states(self):
        newtrans = copy.copy(self)
        newtrans.access_class = copy.copy(self.access_class)
        newtrans.access = copy.copy(self.access)
        newtrans.inMsg = copy.copy(self.inMsg)
        newtrans.outMsg = copy.copy(self.outMsg)
        newtrans.operation = copy.copy(self.operation)
        newtrans.cond = copy.copy(self.cond)
        return newtrans

    ####################################################################################################################
    # HieraGen functions
    ####################################################################################################################

    def update_state_str(self, str_id: str):
        self.update_start_state_id(str_id)
        self.update_final_state_id(str_id)

    def update_start_state_id(self, str_id: str):
        self.startState.state = str_id + "_" + self.startState.state

    def update_final_state_id(self, str_id: str):
        self.finalState.state = str_id + "_" + self.finalState.state

    ####################################################################################################################
    # PROTOGEN FUNCTIONS
    ####################################################################################################################

    def replaceguard(self, guard):
        assert isinstance(guard, str)

        if self.access:
            self.access = guard
        else:
            self.refguard = self.inMsg
            if isinstance(self.inMsg, Message):
                self.inMsg.setmsgtype(guard)
            else:
                self.inMsg = guard

    def renameoutmsg(self, curname, newname):
        for outmsg in self.outMsg:
            if outmsg.getmsgtype() == curname:
                outmsg.setmsgtype(newname)
            self.outmsgrename.update({curname: newname})


########################################################################################################################
# DEBUG FUNCTIONS
########################################################################################################################

    def pbase(self):
        return ("Transition:: SS: " + self.startState.pstate() +
                "  FS: " + self.finalState.pstate() +
                " Guard: " + str(self.getguard()))

