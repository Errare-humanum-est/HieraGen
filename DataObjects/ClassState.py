from typing import List, Dict, Tuple
from antlr3.tree import CommonTree

from DataObjects.ClassMessage import Message
from DataObjects.ClassTransition import Transition
from DataObjects.ClassCommClassification import CommunicationClassification


class State:
    def __init__(self, name, access=0, evict=0):

        self.id = id(self)

        # The more access permission the higher the index,
        # e.g. [load, store]; if store permission then also load is granted
        if isinstance(access, list):
            self.access = access
        elif isinstance(access, str):
            self.access = [access]
        else:
            self.access = []

        if isinstance(evict, list):
            self.evict = evict
        elif isinstance(evict, str):
            self.evict = [evict]
        else:
            self.evict = []

        assert isinstance(name, str)
        self.state = name

        self.setTrans: List[Transition] = []

        self.accessMiss = []
        self.accessHit = []

        self.evictMiss = []
        self.evictHit = []

        self.remoteMiss = []
        self.remoteHit = []
        self.dataAck = []

        self.startstateSets = []
        self.endstateSets = []

        self.deferredRespMsg: List[Message] = []
        self.deferredOperations: Dict[Message, List[CommonTree]] = {}

        self.inherited_remote_traces: List['Trace'] = []

    def __str__(self):
        return self.state

    def testaccess(self, access):
        if access in self.access:
            return 1
        return 0

########################################################################################################################
# STATE ID
########################################################################################################################

    def setstatename(self, name: str):
        assert isinstance(name, str)
        self.state = name

    def getstatename(self) -> str:
        return self.state

########################################################################################################################
# STATE TRANSITION
########################################################################################################################
    def addtransitions(self, transitions: [Transition, List[Transition]]) -> List[Transition]:

        hash_transition_list = [trans.get_hash() for trans in self.setTrans]
        transition_list = []
        
        if isinstance(transitions, list):
            for transition in transitions:
                if transition.get_hash() not in hash_transition_list:
                    transition_list.append(transition)
        else:
            if transitions not in hash_transition_list:
                transition_list.append(transitions)

        if transition_list:
            self.setTrans += transition_list
            self.classify_transitions(transition_list)
        return self.setTrans

    def addremotemiss(self, transition: Transition):
        self.setTrans.append(transition)
        self.remoteMiss.append(transition)

    def gettransitions(self) -> List[Transition]:
        return self.setTrans

    def classify_transitions(self, transitions: List[Transition]):
        for transition in transitions:

            if transition.comm_class == CommunicationClassification().local:
                if transition.access in self.access:
                    self.accessHit.append(transition)
                elif transition.access in self.evict:
                    self.evictHit.append(transition)
                else:
                    assert 0, "CLASSIFICATION ERROR"

            elif transition.comm_class == CommunicationClassification().req:
                if transition.access in self.access:
                    self.accessMiss.append(transition)
                elif transition.access in self.evict:
                    self.evictMiss.append(transition)
                else:
                    print("BREAK ERROR")
                    assert 0, "CLASSIFICATION ERROR"

            elif transition.comm_class in CommunicationClassification().rem_summary:
                self.remoteMiss.append(transition)

            elif transition.comm_class in CommunicationClassification().resp_summary:
                self.dataAck.append(transition)

            else:
                assert False, "State could not be classified"

            '''
            access_class = TransitionClassificationFunc.gen_classification(self.access)
            if access_class == TransitionClassificationEnum.access_hit:
                self.accessHit.append(transition)
            elif access_class == TransitionClassificationEnum.access_miss:
                self.accessMiss.append(transition)
            elif access_class == TransitionClassificationEnum.evict_hit:
                self.evictHit.append(transition)
            elif access_class == TransitionClassificationEnum.evict_miss:
                self.evictMiss.append(transition)
            elif access_class == TransitionClassificationEnum.remote_miss:
                self.remoteMiss.append(transition)
            elif access_class == TransitionClassificationEnum.data_ack:
                self.dataAck.append(transition)
            else:
                assert False, "State could not be classified"
                
            '''

    ####################################################################################################################
    # TRANSITION TESTING
    ####################################################################################################################

    def getaccess(self) -> List['Transition']:
        return self.accessHit + self.accessMiss

    def getaccesshit(self) -> List['Transition']:
        return self.accessHit

    def getaccessmiss(self) -> List['Transition']:
        return self.accessMiss

    def getevict(self) -> List['Transition']:
        return self.evictHit + self.evictMiss

    def getevictmiss(self) -> List['Transition']:
        return self.evictMiss

    def getremote(self) -> List['Transition']:
        return self.remoteHit + self.remoteMiss

    def getremotemiss(self) -> List['Transition']:
        return self.remoteMiss

    def getdataack(self) -> List['Transition']:
        return self.dataAck

    ####################################################################################################################
    # PROTOGEN FUNCTIONS
    ####################################################################################################################

    def gettransitionbyguard(self, guard: str) -> [int, 'Transition']:
        for transition in self.setTrans:
            if transition.getguard() == guard:
                return transition
        return 0

    def getmulttransitionsbyguard(self, guard: str) -> List['Transition']:
        rettransitions = []
        for transition in self.setTrans:
            if transition.getguard() == guard:
                rettransitions.append(transition)

        if rettransitions:
            return rettransitions
        else:
            return []

    def replaceremotestate(self, oldremotestate, newremotestate):
        for transition in self.setTrans:
            startstate = transition.getstartstate()
            finalstate = transition.getfinalstate()

            if startstate == oldremotestate:
                transition.setstartstate(newremotestate)

            if finalstate == oldremotestate:
                transition.setfinalstate(newremotestate)

    ####################################################################################################################
    # PROTOGEN FUNCTIONS
    ####################################################################################################################

    def add_inherited_traces(self, traces: List['Trace']):
        self.inherited_remote_traces += traces

    def test_inherited_trace(self, trace: 'Trace') -> bool:
        if trace in self.inherited_remote_traces:
            return True
        return False

    def filter_remote_traces(self, traces: List['Trace']) -> List['Trace']:
        inherited_trace_hashes = [hash(trace) for trace in self.inherited_remote_traces]
        return [trace for trace in traces if hash(trace) not in inherited_trace_hashes]


########################################################################################################################
# STATE SET
########################################################################################################################
    def addstartstateset(self, state):
        if isinstance(state, list):
            states = state
        else:
            states = [state]

        for entry in states:
            if entry not in self.startstateSets:
                self.startstateSets.append(entry)

        return self.startstateSets

    def addendstateset(self, state):
        if isinstance(state, list):
            states = state
        else:
            states = [state]

        for entry in states:
            if entry not in self.endstateSets:
                self.endstateSets.append(entry)

        return self.endstateSets

    def getstatesets(self):
        return self.startstateSets + self.endstateSets

    def getstartstatesets(self):
        return self.startstateSets

    def getendstatesets(self):
        return self.endstateSets

    def removestateset(self, stateset):
        if stateset in self.startstateSets:
            self.startstateSets.remove(stateset)
        if stateset in self.endstateSets:
            self.endstateSets.remove(stateset)

########################################################################################################################
# PENDING MESSAGES
########################################################################################################################

    def getdefermessages(self) -> List[Message]:
        return self.deferredRespMsg

    def add_head_list_defer_msg_operations(self, message_tuple_list: List[Tuple[Message, List[CommonTree]]]):
        add_defer_msg_list = []

        for message_tuple in message_tuple_list:
            assert message_tuple[0] not in self.deferredRespMsg and message_tuple[0] not in add_defer_msg_list,\
                "Message deferral duplication"
            add_defer_msg_list.append(message_tuple[0])
            self.deferredOperations[message_tuple[0]] = message_tuple[1]

        self.deferredRespMsg = add_defer_msg_list + self.deferredRespMsg

    def add_tail_list_defer_msg_operations(self, message_tuple_list: List[Tuple[Message, List[CommonTree]]]):
        for message_tuple in message_tuple_list:
            assert message_tuple[0] not in self.deferredRespMsg, "Message deferral duplication"
            self.deferredRespMsg.append(message_tuple[0])
            self.deferredOperations[message_tuple[0]] = message_tuple[1]

    def get_defer_msg_operation(self) -> List[Tuple[Message, List[CommonTree]]]:
        message_defer_tuple_list = []
        for message in self.deferredRespMsg:
            message_defer_tuple_list.append((message, self.deferredOperations[message]))
        return message_defer_tuple_list

    def get_defer_msg_operations(self):
        defer_operations = []
        for msg in self.deferredRespMsg:
            for operation in self.deferredOperations[msg]:
                if operation not in defer_operations:
                    defer_operations.append(operation)
        return defer_operations

########################################################################################################################
# POST CLASSIFICATION FUNCTIONS
########################################################################################################################

    def testexclusive(self):
        for transition in self.accessHit:
            if transition.getaccess() == self.access[1]:
                return 1
        return 0

    def getnraccess(self):
        return len(self.accessMiss) + len(self.accessHit)

    def getnrremote(self):
        return len(self.remoteMiss) + len(self.remoteHit)

########################################################################################################################
# DEBUG
########################################################################################################################

    def get_access_str(self) -> List[str]:
        return self.access

    def get_evict_str(self) -> List[str]:
        return self.evict

    def pstate(self):
        return self.state

    def pbase(self):
        return "State:: Name:" + self.state + "  *Access: " + str(self.access)
