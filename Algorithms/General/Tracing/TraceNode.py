from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition
from typing import List


class TraceNodeObj:

    def __init__(self, state: [str, List[str], State], transition: [int, Transition] = 0):
        self.state = state
        self.transition = transition

    def __str__(self):
        return str(self.state) + ("\\ " + str(self.transition) if self.transition else '')

    def get_state(self) -> [str, List[str], State]:
        return self.state

    def get_transition(self) -> [int, Transition]:
        return self.transition
