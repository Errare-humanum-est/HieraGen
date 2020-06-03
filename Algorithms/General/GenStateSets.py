from typing import List, Dict

from DataObjects.ClassStateSet import StateSet
from Parser.ClassProtoParser import ProtoParser
from Algorithms.General.Tracing.TraceTree import *
from Monitor.ProtoCCTable import *


# Handling as a simple dictionary is legacy to ProtoGen Algorithm
class StateSets(dict):

    def __init__(self, *args):
        dict.__init__(self, args)

    def get_states(self) -> Dict[str, State]:
        statedict = {}
        for stateset in self.values():
            states = stateset.getstates()
            for state in states:
                statedict.update({state.getstatename(): state})
        return statedict

    def get_stable_states(self) -> List[State]:
        stablestates = []
        for stateset in self.values():
            stablestates.append(stateset.getstablestate())
        return stablestates


########################################################################################################################
# 2) STATE SET GENERATION --> GenStateSets.py
########################################################################################################################

def create_statesets(states: Dict[str, State], stablestates: List[str]) -> StateSets:
    stateset = StateSets()

    for stablestate in stablestates:
        state = states.get(stablestate, 0)
        cset = StateSet(stablestate, state)
        stateset.update({stablestate: cset})
        state.addendstateset(cset)

    return stateset


########################################################################################################################
# 3) STATE SET ASSIGNMENT -- CC/DC
########################################################################################################################

# Updates the statesets
def assign_statesets(statesets: Dict[str, StateSet], parser: ProtoParser, arch: str, stablestates: List[str]):
    cache_ids = parser.getCacheIdentifiers()
    dir_ids = parser.getDirIdentifiers()
    mem_ids = parser.getMemIdentifiers()
    access = parser.getAccess() + parser.getEvict()

    traces = []
    for stateset in statesets:
        settraces: List[List[TraceNodeObj]] = create_trace_tree(statesets[stateset].getstablestate(), stablestates)
        if arch in cache_ids:
            cache_trace_assignment(access, settraces, statesets)
        elif arch in dir_ids:
            directory_trace_assignment(access, settraces, statesets)
        elif arch in mem_ids:
            directory_trace_assignment(access, settraces, statesets)
        else:
            perror('Unknown architecture', 0)

        traces += settraces
    return traces


def cache_trace_assignment(accessids: List[str], traces: List[List[TraceNodeObj]], statesets: Dict[str, StateSet]):
    backward_search(accessids, traces, statesets)
    forward_search(traces)
    return statesets


def directory_trace_assignment(accessids: List[str], traces: List[List[TraceNodeObj]], statesets: Dict[str, StateSet]):
    backward_search(accessids, traces, statesets)
    return statesets


def backward_search(accessids: List[str], traces: List[List[TraceNodeObj]], statesets: Dict[str, StateSet]):
    remoterequests = remote_requests(statesets)
    # Run backwards
    for trace in traces:
        # The length of the trace is startstate, n*transientstates, endstate
        # A trace of length 2 only encompasses start and endstate and can therefore be ignored
        if len(trace) > 2:

            startset = trace[-1].get_state().getstatesets()[0]
            endset = trace[0].get_state().getstatesets()[0]

            for ind in range(0, len(trace) - 1):
                transition = trace[ind].get_transition()

                trans_access = transition.getaccess()
                guard = transition.getguard()
                finalstate = transition.getfinalstate()

                # Alternatively this could also be derived from transition.comm_class == request
                if guard and trans_access in accessids:
                    startset.addstartstate(finalstate)
                    endset.addendstate(finalstate)

                else:
                    endset.addendstate(finalstate)

                    if [remoterequest for remoterequest in remoterequests if guard == remoterequest]:
                        endset = update_endset(guard, endset, statesets)


def forward_search(traces: List[List[TraceNodeObj]]):
    for trace in traces:
        if len(trace) > 2:
            startsets = [trace[-1].get_state().getstatesets()[0]]

            for ind in range(len(trace) - 2, 0, -1):
                transition = trace[ind].get_transition()

                guard = transition.getguard()
                finalstate = transition.getfinalstate()

                newset = search_set_guard(startsets, guard, finalstate)

                if newset:
                    startsets = [newset]
                else:
                    startsets = finalstate.getstatesets()


def search_set_guard(startsets, guard, finalstate):
    for startset in startsets:
        for remoterequest in startset.getstablestate().getremote():
            if guard == remoterequest.getguard():
                newset = remoterequest.getfinalstate().getstatesets()[0]
                newset.addstartstate(finalstate)
                return newset
    return 0


def remote_requests(statesets):
    remoterequests = []
    for stateset in statesets:
        transitions = statesets[stateset].getstablestate().getremote()

        for transition in transitions:
            remoterequests.append(transition.getguard())

    return list(set(remoterequests))


def update_endset(guard, endset, statesets):
    for stateset in statesets:
        transitions = statesets[stateset].getstablestate().getremote()

        for transition in transitions:
            if transition.getguard() == guard and transition.getfinalstate() == endset.getstablestate():
                return statesets[stateset]

    return endset


########################################################################################################################
# MISC
########################################################################################################################

def extract_states_from_sets(statesets):
    statedict = {}
    for stateset in statesets:
        states = statesets[stateset].getstates()
        for state in states:
            statedict.update({state.getstatename(): state})
    return statedict


def get_stable_states(statesets):
    stablestates = []
    for stateset in statesets:
        stablestates.append(statesets[stateset].getstablestate())
    return stablestates
