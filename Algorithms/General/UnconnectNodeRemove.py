from typing import List
from DataObjects.ClassTransition import Transition
from DataObjects.ClassState import State

def remove_unconnected_nodes(transitions: List[Transition]) -> List[Transition]:
    start_states: List[State] = []
    final_states: List[State] = []
    for transition in transitions:
        if transition.startState != transition.finalState:
            start_states.append(transition.startState)
            final_states.append(transition.finalState)

    # Perform quick terminal state check
    assert not set(start_states).symmetric_difference_update(set(final_states)), "Error Terminal States found"

    # Return filtered transitions
    return [transition for transition in transitions if transition.startState in start_states]
