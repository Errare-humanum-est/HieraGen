import copy
from typing import List

from DataObjects.ClassTransition import Transition

from Algorithms.General.AuxStateHandler import AuxStateHandler
from Algorithms.General.GenDeferMessage import GenDeferMessage

from Murphi.MurphiModular import MurphiModular


class HieraMergeFunc:
    def __init__(self):
        pass

    ''' 
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    THE MESSAGES BELOW DIRECTLY MODIFY THE TRANSITIONS AND OPERATION FIELDS ACCORDING TO MURPHI FRAMEWORK REQUIREMENTS
    TO DEFER DATA
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ####################################################################################################################
    # MESSAGE DEFERRING FUNCTIONS
    ####################################################################################################################
    '''

    @staticmethod
    def type_copy(val1, val2):
        return copy.copy(val1) + copy.copy(val2)

    def conservative_level_merge(self,
                                 first_transitions: List[Transition], second_transitions: List[Transition],
                                 defer_push_token: str, defer_pop_token: str) \
            -> List[Transition]:

        self.msg_defer_generation(first_transitions, second_transitions, defer_push_token, defer_pop_token)

        if not first_transitions[0].outMsg:
            return self.first_immediate_merge(first_transitions, second_transitions)
        else:
            return self.first_not_immediate_merge(first_transitions, second_transitions)

    def first_immediate_merge(self,
                              first_transitions: List[Transition], second_transitions: List[Transition]) \
            -> List[Transition]:
        # The level (first transitions) to which the request is directed does not need to perform an access
        # After the first level has completed its local access, return the data to the
        # requestor level (second transitions)
        # Msg deferring must be also done in case of immediate merge, because of how the if else tree construction and
        # the nesting in the backend works, but is in case of an immediate response logically not necessary
        second_transitions[0].startState = first_transitions[0].startState
        second_transitions[0].operation = self.type_copy(first_transitions[0].operation,
                                                         second_transitions[0].operation)
        return second_transitions

    def first_not_immediate_merge(self,
                                  first_transitions: List[Transition], second_transitions: List[Transition]) \
            -> List[Transition]:
        # First perform remote level access
        # For the HL access, put directory access message as trigger and defer the high level access requestor
        # information
        first_transitions[0].inMsg = second_transitions[0].inMsg
        second_transitions[0].inMsg = first_transitions[-1].inMsg
        second_transitions[0].operation = self.type_copy(first_transitions[-1].operation,
                                                         second_transitions[0].operation)
        second_transitions[0].startState = first_transitions[-1].startState

        return first_transitions[:-1] + second_transitions

    def msg_defer_generation(self,
                             first_transitions: List[Transition], second_transitions: List[Transition],
                             defer_push_token: str, defer_pop_token: str):
        # Defer a copy of the remote request message and issue internal operations
        first_transitions[0].operation = self.type_copy(
            [GenDeferMessage().defer_push_message(second_transitions[0], defer_push_token)],
            first_transitions[0].operation)

        new_operation = GenDeferMessage().defer_pop_message(second_transitions[0], defer_pop_token)

        second_transitions[0].operation = [new_operation] + copy.copy(second_transitions[0].operation)

        # Rename the variables
        AuxStateHandler.cond_operations_var_rename(second_transitions[0].operation, str(second_transitions[0].inMsg),
                                                   MurphiModular.vdeferpref + str(second_transitions[0].inMsg))

