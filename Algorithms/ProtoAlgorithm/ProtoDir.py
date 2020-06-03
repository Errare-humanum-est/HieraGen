import copy

from typing import List, Tuple

from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition
from DataObjects.ClassArchitecture import Architecture
from DataObjects.ClassMessage import Message

from Algorithms.ProtoAlgorithm.ProtoBase import ProtoBase

from Algorithms.General.Tracing.TraceTree import create_trace_tree
from antlr3.tree import CommonTree

class ProtoDir(ProtoBase):

    def __init__(self):
        ProtoBase.__init__(self)
        self.nonstalling = False
        self.progressMessages = None
        self.DCconservativeInv = False


########################################################################################################################
#   TRANSIENT STATE GENERATION
########################################################################################################################

    def _GenerateTransientStates(self, arch: Architecture, statesets, stablestates, deferfunc):

        newstates = []

        statedict = {}

        for stateset in statesets:
            statedict.update({stateset: copy.copy(statesets[stateset].getstates())})

        for stateset in statesets:
            stablestate = statesets[stateset].getstablestate()

            # Get possible remote transitions for this stable state
            remotetrans = stablestate.getremote()

            # Iterate over all remote transitions
            for transition in remotetrans:

                # Iterate over all the transient states of the current state set
                for state in statedict[stateset]:

                    # Check if a transition with the same guard already exists
                    exist_trans = state.getmulttransitionsbyguard(transition.getguard())

                    # if a transition exists, check if the state conditions match, if not create a new transition
                    # sequence
                    if not transition.getcond() in [ref_trans.getcond() for ref_trans in exist_trans]:
                        newstates += self._TransientStateInheritance(arch,
                                                                     transition,
                                                                     state,
                                                                     statesets[stateset],
                                                                     stablestates,
                                                                     deferfunc)

        return newstates

    def _TransientStateInheritance(self, arch: Architecture,
                                   transition: Transition,
                                   state,
                                   stateset,
                                   stablestates,
                                   deferfunc) -> List[State]:
        new_states = []

        # Test if the message is a serialization message or any other control message
        # In the non-stalling configuration control messages are deferred if control dependencies exist,
        # else they are served immediately
        if not self.nonstalling:
            if not self.test_serialization_msg(transition):
                return new_states

        finalsets = transition.getfinalstate().getstatesets()


        # Rule if a remote transition exists in the startstate and finalstate having the same guard, the message
        # is considered to be unrelated to the current state and will be therefore ignored until a stable state is
        # reached

        # Test if final stable state or remote transition is startstate of current stateset
        if state in stateset.getstartstates():
            # Serialized before own transaction
            # Find path startstate to state
            guards = self._FindAccessTrace(state, stateset, stablestates)

            # Find new final state
            finalstate = self._SetGuardSearch(guards, finalsets)
            if finalstate:
                state.addtransitions(self._CopyModifyTransition(transition, state, finalstate))
            else:
                new_states.append(self._CopyModifyState(state, transition))

        else:
            # Serialized after own transaction
            if self.nonstalling:
                # Cache and directory dependent. Only if they have data
                # Transition start and final state do not change, however,
                # responses might be deferred due to data dependencies
                if transition.getstartstate() == transition.getfinalstate() and state in stateset.getendstates():
                    pass
                    # ANALYZE DEPENDENCY OF CURRENT TRANSITION AND VARIABLES THAT ARE DEPENDENT.
                    # IF THERE EXISTS A DEPENDENCY NO LOOPING IS ALLOWED
                    '''
                    newtrans = self._CopyModifyTransition(transition, state, state)
                    # Defer message
                    defermsg = deferfunc(transition, newtrans)
                    if defermsg:
                        new_state = self._GenerateState(state, transition, stablestates, deferfunc)
                        if new_state:
                            new_states.append(new_state)
                    else:
                        state.addtransitions(newtrans)
                    '''
                else:
                    # A new state needs to be created
                    new_state = self._GenerateState(state,
                                                    transition,
                                                    stablestates,
                                                    deferfunc)
                    if new_state:
                        new_states.append(new_state)

        return new_states

    def test_serialization_msg(self, transition: Transition) -> bool:
        # Rule if a remote transition exists in the stable startstate and stable finalstate having the same guard,
        # the message is considered NOT to be a serialization message and therefore to be unrelated to the current state
        # and will be therefore ignored until a stable state is reached if the ProtoGen works in the stalling mode or
        # handled if no data dependencies exist in the non-stalling mode
        guard = str(transition.getguard())
        if (self.state_guard_search(guard, transition.startState) and
                self.state_guard_search(guard, transition.finalState)):
            return False
        return True

    ####################################################################################################################
    # STARTSTATE INHERITANCE
    ####################################################################################################################
    # Don't use SSP traces from level, because a new state might have been created in the meantime that satisfies the
    # trace conditions already
    def _FindAccessTrace(self, state, stateset, stablestates):
        # Create all traces from current stable state
        traces = create_trace_tree(stateset.getstablestate(), stablestates)
        for trace in traces:
            guards = []
            for ind in range(len(trace) - 2, 0, -1):
                guards.append(trace[ind].get_transition().getguard())
                if trace[ind].get_state() == state:
                    return guards
        return 0

    def _CopyModifyState(self, startstate, transition):
        newstate = State(startstate.getstatename() + "_" + transition.getguard(), self.access, self.evict)
        for datatrans in startstate.getdataack():
            newtrans = copy.copy(datatrans)
            newtrans.setstartstate(newstate)
            newstate.addtransitions(newtrans)

        for startset in transition.getfinalstate().getstatesets():
            startset.addstartstate(newstate)

        for endset in startstate.getendstatesets():
            endset.addendstate(newstate)

        # Create vertice
        startstate.addtransitions(self._CopyModifyTransition(transition, startstate, newstate))

        return newstate


    ####################################################################################################################
    # COMMON
    ####################################################################################################################

    @staticmethod
    def _DeepCopyModifyTransitionOperation(transition: Transition, startstate: State, finalstate: State) -> Transition:
        newtrans = copy.copy(transition)
        newtrans.setstartstate(startstate)
        newtrans.setfinalstate(finalstate)
        newtrans.operation = copy.copy(transition.operation)
        return newtrans

    def state_guard_search(self, guard: str, state: State) -> bool:
        for transition in state.setTrans:
            if str(transition.getguard()) == guard:
                return True
        return False


    ####################################################################################################################
    # SERIALIZED AFTER => FINALSTATE INHERITANCE
    ####################################################################################################################

    def _GenerateState(self, fork_state, remote_transition, stablestates, deferfunc):
        newstates: List[State] = []

        finalsets = remote_transition.getfinalstate().getstatesets()
        if len(finalsets) > 1:
            print("Attention")
            return None

        newtrans = self._DeepCopyModifyTransitionOperation(remote_transition, fork_state, fork_state)

        # Defer message
        defer_tuples = deferfunc(remote_transition, newtrans)

        unique_dummy_state = State("Placeholder")

        newstate = self._CopyState(fork_state,
                                   remote_transition.getguard(),
                                   finalsets[0],
                                   stablestates,
                                   newstates,
                                   unique_dummy_state,
                                   defer_tuples)

        newtrans.setfinalstate(newstate)
        fork_state.addremotemiss(newtrans)

        # ADD DEFER TRANSITIONS TO THE FIELD SINCE THERE EXIST TRACES THAT NEED TO BE STORED,
        # THINK ABOUT NOT SINGLE TRANSITION REMOTE REQUESTS

        # If the remote transition is part of a longer trace, it is deferred
        # Take the last new_state
        for newstate in newstates:
            for transition in newstate.setTrans:
                if transition.finalState == unique_dummy_state:
                    if defer_tuples:
                        transition.outMsg = copy.copy(transition.outMsg)
                        transition.operation = copy.copy(transition.operation)
                        # Add defer operation to remote_transition
                        for defer_tuple in defer_tuples:
                            transition.addoutmsg(defer_tuple[0])
                            transition.add_operation_list(defer_tuple[1])
                    # Set final state to remote_transition final state
                    transition.finalState = remote_transition.finalState


        return newstate

    def _CopyState(self,
                   startstate: State,
                   guard,
                   stateset,
                   stablestates,
                   newstates,
                   dummy_state,
                   defer_operations: List[Tuple[Message, List[CommonTree]]] = None):
        newstate = State(self._CheckStateName(startstate.getstatename() + "__"
                                              + guard + "_"
                                              + stateset.getstablestate().getstatename(),
                                              stateset),
                         self.access, self.evict)

        newstates.append(newstate)
        stateset.addendstate(newstate)

        #newstate.add_tail_list_defer_msg_operations(copy.copy(startstate.get_defer_msg_operation()))

        if defer_operations:
            newstate.add_tail_list_defer_msg_operations(defer_operations)

        for transition in startstate.getdataack():
            newtrans = copy.copy(transition)
            # Emit non deferred messages
            #newtrans.add_out_msg_list(copy.copy(transition.getoutmsg()))
            newtrans.setstartstate(newstate)

            if transition.getstartstate() == transition.getfinalstate():
                newtrans.setfinalstate(newstate)
            else:
                finalstate = [finalstate for finalstate in stablestates
                              if finalstate == newtrans.getfinalstate().getstatename()]
                if finalstate:
                    newtrans.setfinalstate(dummy_state)

                else:
                    finalstate = self._CopyState(newtrans.getfinalstate(),
                                                 guard,
                                                 stateset,
                                                 stablestates,
                                                 newstates,
                                                 dummy_state,
                                                 defer_operations)

                    newtrans.setfinalstate(finalstate)
            newstate.addtransitions(newtrans)
        return newstate

    def _CheckStateName(self, name, stateset):
        for state in stateset.getstates():
            if state.getstatename() == name:
                return name + "_"
        return name

    def _DirectoryDefer(self, transition, newtrans):
        if self.DCconservativeInv:
            return newtrans.deferoutmsg()
        else:
            res = self._AccessDetection(self.cacheStateSets)

            evictmsgs = []
            for refval in res[1].values():
                evictmsgs += refval

            if not [msgtype for msgtype in evictmsgs if msgtype == transition.getguard()]:
                return newtrans.deferoutmsg(self.progressMessages), None
        return 0
