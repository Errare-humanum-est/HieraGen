from typing import List, Dict

import copy

from Parser.ForkTree import ForkTree
from Algorithms.General.Tracing.TraceNode import TraceNodeObj

from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition


class TraceSet:

    def __init__(self, traces: List[List[TraceNodeObj]]):
        self.start_state_dict: Dict[State, List[Trace]] = {}
        self.final_state_dict: Dict[State, List[Trace]] = {}
        for trace in traces:
            trace_obj = Trace(trace)
            startstate = trace_obj.startstate
            if startstate in self.start_state_dict:
                self.start_state_dict[startstate] += [trace_obj]
            else:
                self.start_state_dict[startstate] = [trace_obj]

            finalstate = trace_obj.finalstate
            if finalstate in self.final_state_dict:
                self.final_state_dict[finalstate] += [trace_obj]
            else:
                self.final_state_dict[finalstate] = [trace_obj]


class Trace:
    def __init__(self, node_obj_list: List[TraceNodeObj]):
        self.trace: List[TraceNodeObj] = list(reversed(node_obj_list))
        self.states: List[State] = []
        self.transitions: List[Transition] = []
        self.access: List[str] = []
        self.outmsg: List[str] = []
        self.inmsg: List[str] = []
        self.startstate = None
        self.finalstate = None

        self.orig_traces = [self]

        self.update_messages_and_states()

        assert len(self.access) <= 1, "More than one access per trace"

        self.update_final_states()

    def __str__(self):
        state_str = str(self.startstate)
        for ind in range(1, len(self.trace)):
            if self.trace[ind].transition:
                state_str += " -" + str(self.trace[ind].transition).split('-', 1)[1]
        return state_str

    def __hash__(self):
        return hash(tuple((id(transition) for transition in self.transitions)))

    '''
    def __eq__(self, other: 'Trace'):
        if isinstance(other, Trace):
            if set(self.states) == set(other.states) and set(self.transitions) == set(other.transitions) and \
                set(self.access) == set(other.access) and set(self.outmsg) == set(other.outmsg) and \
                set(self.inmsg) == set(other.inmsg) and self.startstate == other.startstate and \
                    self.finalstate == other.finalstate:
                return True
        return False
    '''

    def __add__(self, other: 'Trace'):
        new_trace = copy.copy(self)
        new_other = copy.copy(other)

        new_trace.trace = new_trace.trace + new_other.trace
        new_trace.states = copy.copy(new_trace.states)
        new_trace.transitions = copy.copy(new_trace.transitions)
        new_trace.outmsg = copy.copy(new_trace.outmsg)
        new_trace.inmsg = copy.copy(new_trace.inmsg)
        new_trace.access = copy.copy(new_trace.access)

        for state in new_other.states:
            if state not in new_trace.states:
                new_trace.states.append(state)

        new_trace.update_messages_and_states()
        new_trace.update_final_states()
        new_trace.orig_traces = self.orig_traces + other.orig_traces

        return new_trace

    @staticmethod
    def constr_trace_from_trans(trans: Transition):
        trace = Trace([])
        trace.states = [trans.startState, trans.finalState]
        trace.transitions.append(trans)
        trace.access = trans.access
        trace.outmsg = trans.outMsg
        trace.inmsg = [trans.inMsg] if trans.inMsg else []
        trace.startstate = trans.startState
        trace.finalstate = trans.finalState

        return trace

    def comp_traces(self, other: 'Trace') -> bool:
        if set(self.transitions) == set(other.transitions):
            return True
        return False

    def comp_trace_list(self, other: List['Trace']) -> List['Trace']:
        match_traces = []
        for trace in other:
            if set(self.transitions) == set(trace.transitions):
                match_traces.append(trace)
        return match_traces

    def trans_hash(self):
        return hash(tuple([trans.get_hash() for trans in self.transitions]))

    def update_messages_and_states(self):
        for entry in self.trace:
            if entry.transition:
                if entry.transition not in self.transitions:
                    self.transitions.append(entry.transition)

                    # Update the state tracking
                    if entry.transition.startState not in self.states:
                        self.states.append(entry.transition.startState)
                    if entry.transition.finalState not in self.states:
                        self.states.append(entry.transition.finalState)

                    self.outmsg += entry.transition.getoutmsgtypes()
                    if entry.transition.getinmsg():
                        self.inmsg.append(entry.transition.getinmsg())
                    if entry.transition.getaccess():
                        self.access.append(entry.transition.getaccess())

    def update_final_states(self):
        if self.trace:
            self.startstate = self.trace[0].state
            self.finalstate = self.trace[-1].state

    def get_start_state(self):
        return self.startstate

    def get_final_state(self):
        return self.finalstate

    def get_inmsg_str_list(self):
        return [str(inmsg) for inmsg in self.inmsg]

    def get_outmsg_str_list(self):
        return [str(outmsg) for outmsg in self.outmsg]

    def copy_modify_trace(self, startstate: State, finalstate: State = None):
        new_final_state = self.finalstate
        if not finalstate:
            new_final_state = finalstate

        newtrace = copy.copy(self)

        # Start state
        newtrace.trace[0].state = startstate
        newtrace.trace[1].transition = \
            newtrace.trace[1].transition.copy_modify_trans(startstate, newtrace.trace[1].transition.finalState)
        # Final state
        newtrace.trace[-1].state = new_final_state
        newtrace.trace[1].transition = \
            newtrace.trace[-1].transition.copy_modify_trans(newtrace.trace[-1].transition.startState, new_final_state)

        self.update_final_states()


########################################################################################################################
# TRACE TREE
########################################################################################################################
# Creates all traces connecting the stable states
def create_stable_state_traces(statesets: 'StateSets'):
    stable_states = statesets.get_stable_states()
    stable_state_id = [str(state) for state in stable_states]
    traces = []
    for state in stable_states:
        traces += create_trace_tree(state, stable_state_id)
    return traces


# Create tree from (stable) state to states whose name is element of the stablestatelist
def create_trace_tree(state: State, stablestates: List[str]) -> List[List[TraceNodeObj]]:

    tracetree = ForkTree()

    basenode = tracetree.insertnode(TraceNodeObj(state))

    # Initially get loops from states once
    nextlist = get_trans_finalstates_loop([basenode], state.gettransitions())

    while nextlist:
        endnodes = []
        for nextnode in nextlist:
            endnodes += tracetree.appenddata(nextnode[1], nextnode[0])

        nextlist = []
        for node in endnodes:
            state = node.getdata().get_state()
            if not [stateid for stateid in stablestates if state.getstatename() == stateid]:
                nextlist += get_trans_finalstates([node], state.gettransitions())

    return tracetree.gettraces()


def get_trans_finalstates(nodes, transitions):
    nextlist = []

    for node in nodes:
        state = node.getdata().get_state()
        nextstates = []
        predecessor_trans = []

        cur_node = node
        while cur_node.predecessor:
            cur_trans = cur_node.predecessor.data.transition
            if cur_trans:
                predecessor_trans.append(str(cur_trans.startState))
            cur_node = cur_node.predecessor

        for transition in transitions:
            finalstate = transition.getfinalstate()
            if finalstate != state:
                if str(node.data.transition.finalState) not in predecessor_trans:
                    nextstates.append(TraceNodeObj(finalstate, transition))

        nextlist.append([node, nextstates])

    return nextlist


# Create tree from (stable) state to states whose name is element of the stablestatelist
def create_loop_trace_tree(state: State, stablestates: List[str]) -> ForkTree:

    tracetree = ForkTree()

    basenode = tracetree.insertnode(TraceNodeObj(state))

    nextlist = get_trans_finalstates_loop([basenode], state.gettransitions())

    while nextlist:
        endnodes = []
        for nextnode in nextlist:
            endnodes += tracetree.appenddata(nextnode[1], nextnode[0])

        nextlist = []
        for node in endnodes:
            state = node.getdata().get_state()
            if not [stateid for stateid in stablestates if state.getstatename() == stateid]:
                nextlist += get_trans_finalstates([node], state.gettransitions())

    return tracetree.gettraces()


def get_trans_finalstates_loop(nodes, transitions):
    transitions = list(set(transitions))
    nextlist = []

    for node in nodes:
        nextstates = []
        successor_trans = []

        cur_node = node
        while cur_node.predecessor:
            successor_trans.append(cur_node.predecessor.data.transition)
            cur_node = cur_node.predecessor

        state = node.getdata().get_state()
        for transition in transitions:
            finalstate = transition.getfinalstate()
            if finalstate != state:
                nextstates.append(TraceNodeObj(finalstate, transition))
            else:
                if node.data.transition not in successor_trans:
                    nextstates.append(TraceNodeObj(finalstate, transition))

        nextlist.append([node, nextstates])

    return nextlist
