from typing import Dict, List

from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition
from Parser.ClassProtoParser import ProtoParser

from Monitor.ProtoCCTable import *

''' Functions parse input from Parser and generate State objects'''


########################################################################################################################
# 1) INPUT PROCESSING -- CC/DC
########################################################################################################################

# Creates the state objects that contain its corresponding transitions
def create_states(transitions: List[Transition], access: List[str], evict: List[str]) -> Dict[str, State]:
    states = convert_statenodes_to_states(transitions, access, evict)
    update_transitions(states, transitions)
    return states


# Sorts the states given in all initial transitions given in parser
def sort_states(transitions: List[Transition]) -> Dict[str, List[Transition]]:
    statetransmap = {}
    startnames = []
    finalnames = []

    for transition in transitions:
        startstate = transition.getstartstate().getstatename()
        finalstate = transition.getfinalstate().getstatename()

        if startstate != finalstate:
            startnames.append(startstate)
            finalnames.append(finalstate)

        if startstate in statetransmap:
            statetransmap.update({startstate: statetransmap[startstate] + [transition]})
        else:
            statetransmap.update({startstate: [transition]})

    # Make seperate sanity check function
    #startset = set(startnames)
    #finalset = set(finalnames)

    #perror("Terminal state found in input description: " + str(startset.symmetric_difference(finalset)),
    #       startset == finalset)

    return statetransmap


# Convert StateNode objects from Parser to State objects used by Algorithm
def convert_statenodes_to_states(transitions: List[Transition], access: List[str], evict: List[str]) -> Dict[str, State]:
    states = {}
    statetransmap = sort_states(transitions)
    for statename in statetransmap:
        # Create a new state object
        states.update({statename: State(statename, access, evict)})
        states[statename].addtransitions(statetransmap[statename])
    return states


# Replace StateNode objects of parser with new created State objects
# This points each Transition to its start and end State and points the State objects to their Transition as well
def update_transitions(states: Dict[str, State], transitions: List[Transition]):
    for transition in transitions:
        transition.setstartstate(states[transition.getstartstate().getstatename()])
        try:
            transition.setfinalstate(states[transition.getfinalstate().getstatename()])
        except KeyError:
            print("STOP")
