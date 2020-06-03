from typing import List, Dict

from DataObjects.ClassState import State
from DataObjects.ClassTransition import Transition


class HieraStateRenameGen:
    def __init__(self):
        self.cc_dir_to_cc_state_map: Dict[State, List[State]] = {}
        self.cc_dir_to_dir_state_map: Dict[State, List[State]] = {}

    ####################################################################################################################
    # State rename transition
    ####################################################################################################################

    def rename_cc_states(self, renamed_states: Dict[State, State], transitions: List[Transition], dir_state: State,
                         prefix=""):
        for ind in range(0, len(transitions)):
            transition = transitions[ind]
            if ind == 0:
                self.rename_start_state_add_dir(renamed_states, transition, dir_state)
            else:
                self.rename_start_state_add_dir(renamed_states, transition, dir_state, prefix)

            if ind == len(transitions) - 1:
                self.rename_final_state_add_dir(renamed_states, transition, dir_state)
            else:
                self.rename_final_state_add_dir(renamed_states, transition, dir_state, prefix)

    def rename_dir_states(self, renamed_states: Dict[State, State], transitions: List[Transition], cc_state: State,
                          prefix=""):
        for ind in range(0, len(transitions)):
            transition = transitions[ind]
            if ind == 0:
                self.rename_start_state_add_cc(renamed_states, cc_state, transition)
            else:
                self.rename_start_state_add_cc(renamed_states, cc_state, transition, prefix)

            if ind == len(transitions) - 1:
                self.rename_final_state_add_cc(renamed_states, cc_state, transition)
            else:
                self.rename_final_state_add_cc(renamed_states, cc_state, transition, prefix)

    def rename_start_state_add_dir(self, rename_state_list: Dict[State, State], cc_transition: Transition,
                                   dir_state: State,
                                   prefix=""):
        if isinstance(cc_transition.startState, list):
            start_state = cc_transition.startState[0]
        else:
            start_state = cc_transition.startState
        cc_state_str = prefix + self.new_state_name(dir_state.state, start_state.state)
        cc_transition.startState = self.cc_dir_state(rename_state_list, cc_state_str, start_state)
        if isinstance(cc_transition.startState, list):
            for start_state in cc_transition.startState:
                self.add_to_dict_list(self.cc_dir_to_cc_state_map, cc_transition.startState, start_state)
        else:
            self.add_to_dict_list(self.cc_dir_to_cc_state_map, cc_transition.startState, start_state)

    def rename_final_state_add_dir(self, rename_state_list: Dict[State, State], cc_transition: Transition,
                                   dir_state: State,
                                   prefix=""):
        if isinstance(cc_transition.finalState, list):
            start_state = cc_transition.finalState[0]
        else:
            start_state = cc_transition.finalState
        cc_state_str = prefix + self.new_state_name(dir_state.state, start_state.state)
        cc_transition.finalState = self.cc_dir_state(rename_state_list, cc_state_str, start_state)
        if isinstance(cc_transition.finalState, list):
            for start_state in cc_transition.finalState:
                self.add_to_dict_list(self.cc_dir_to_cc_state_map, cc_transition.finalState, start_state)
        else:
            self.add_to_dict_list(self.cc_dir_to_cc_state_map, cc_transition.finalState, start_state)

    def rename_start_state_add_cc(self, rename_state_list: Dict[State, State], cc_state: State,
                                  dir_transition: Transition,
                                  prefix=""):
        if isinstance(dir_transition.startState, list):
            start_state = dir_transition.startState[0]
        else:
            start_state = dir_transition.startState
        dir_state_str = prefix + self.new_state_name(start_state.state, cc_state.state)
        dir_transition.startState = self.cc_dir_state(rename_state_list, dir_state_str, start_state)
        if isinstance(dir_transition.startState, list):
            for start_state in dir_transition.startState:
                self.add_to_dict_list(self.cc_dir_to_dir_state_map, dir_transition.startState, start_state)
        else:
            self.add_to_dict_list(self.cc_dir_to_dir_state_map, dir_transition.startState, start_state)

    def rename_final_state_add_cc(self, rename_state_list: Dict[State, State], cc_state: State,
                                  dir_transition: Transition,
                                  prefix=""):
        if isinstance(dir_transition.finalState, list):
            start_state = dir_transition.finalState[0]
        else:
            start_state = dir_transition.finalState
        dir_state_str = prefix + self.new_state_name(start_state.state, cc_state.state)
        dir_transition.finalState = self.cc_dir_state(rename_state_list, dir_state_str, start_state)
        if isinstance(dir_transition.finalState, list):
            for start_state in dir_transition.finalState:
                self.add_to_dict_list(self.cc_dir_to_dir_state_map, dir_transition.finalState, start_state)
        else:
            self.add_to_dict_list(self.cc_dir_to_dir_state_map, dir_transition.finalState, start_state)

    @staticmethod
    def new_state_name(ll_dir_state_name: str, hl_cache_state_name: str) -> str:
        return ll_dir_state_name + "_x_" + hl_cache_state_name

    @staticmethod
    def add_to_dict_list(object_list, key, cur_object):
        if key in object_list:
            if cur_object not in object_list[key]:
                object_list[key].append(cur_object)
        else:
            object_list[key] = [cur_object]

    @staticmethod
    def cc_dir_state(rename_state_list: Dict[State, State], state_str: str, state: State) -> State:
        if state_str not in rename_state_list:
            cc_dir_state = State(state_str, state.access, state.evict)
            rename_state_list[state_str] = cc_dir_state
            return cc_dir_state
        else:
            return rename_state_list[state_str]
