from typing import List, Dict, Tuple

from DataObjects.ClassTransition import Transition
from DataObjects.ClassMultiDict import MultiDict

from antlr3.tree import CommonTree
from Murphi.MurphiModular import MurphiModular


class GenMsgDepedencyMap:

    def __init__(self,
                 first_transitions: List[Transition], second_transitions: List[Transition],
                 ):
        # Analyze data dependencies between ll_dir response and hl_cache response messages

        # hl_cache receiver data local variable to message variable map
        self.cl_var_to_resp_msg_map_second = self.get_hl_response_var_msg_map(second_transitions)
        self.cl_var_to_resp_operation_map_first, self.cl_var_to_resp_msg_map_first = \
            self.get_dir_response_var_msg_map(first_transitions)

        # Compare the fields
        self.defer_operation_var: Dict[CommonTree, List[str]] = MultiDict()
        for var in self.cl_var_to_resp_operation_map_first:
            # The variable is modified by the external requests
            if var in self.cl_var_to_resp_msg_map_second:
                for operation in self.cl_var_to_resp_operation_map_first[var]:
                    self.defer_operation_var[operation] = [var]

    @staticmethod
    # tASSIGN e.g. cache_line = GetM.src
    def get_hl_response_var_msg_map(second_transitions: List[Transition]) -> MultiDict:
        # Analyze data response messages payload of hl_cc trace
        cl_var_to_resp_msg_map_second = MultiDict()
        for transition in second_transitions:
            in_msg_name = str(transition.inMsg)
            for operation in transition.operation:
                if not str(operation) == MurphiModular.tASSIGN:
                    continue
                children = operation.getChildren()
                if str(children[2]) == in_msg_name:
                    cl_var_to_resp_msg_map_second[str(children[0])] = children[2]
        return cl_var_to_resp_msg_map_second

    @staticmethod
    # tMSGCSTR e.g. local_var = Resp(GetM, .....)
    # tASSIGN e.g. cache_line = GetM.src
    def get_dir_response_var_msg_map(first_transitions: List[Transition]) -> Tuple[MultiDict, MultiDict]:
        # Analyze directory response messages to ll_cc payload of ll_dir trace
        cl_var_to_resp_operation_map_first = MultiDict()
        cl_var_to_resp_msg_map_first = MultiDict()
        for transition in first_transitions:
            for operation in transition.operation:
                if not str(operation) == MurphiModular.tASSIGN:
                    continue
                children = operation.getChildren()
                # Normal messages
                if str(children[2]) == MurphiModular.tMSGCSTR:
                    msg_payload = children[2].getChildren()
                    # msg_format, type, src, dest, payload
                    if len(msg_payload) <= 4:
                        continue
                    for var in msg_payload[4:]:
                        cl_var_to_resp_operation_map_first[str(var)] = operation
                        cl_var_to_resp_msg_map_first[str(var)] = msg_payload[1]
                # Deferred Messages
                #elif str(children[2]) == MurphiModular.tSEND_BASE_DEFER:
                #    pwarning("Untested functionality, WIP")
                #    msg_payload = children[2].getChildren()
                #    # Base_msg, payload
                #    if len(msg_payload) <= 2:
                #        continue
                #    for var in msg_payload[2:]:
                #        cl_var_to_resp_operation_map_first[str(var)] = operation
                #        cl_var_to_resp_msg_map_first[str(var)] = msg_payload[1]

        return cl_var_to_resp_operation_map_first, cl_var_to_resp_msg_map_first

