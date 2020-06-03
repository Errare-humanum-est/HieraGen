from antlr3.tree import CommonTree
from typing import List, Dict

from Parser.ProtoCCcomTreeFct import toStringList
from Parser.CopyReducedCommonTree import copy_tree
from Murphi.ModularMurphi.MurphiTokens import MurphiTokens


class AuxStateHandler:
    def __init__(self, transition: 'Transition'):
        # msg is currently msg_0
        self.var_to_new_var_map: Dict[str, str] = {}
        # e.g. PutM: msg_0
        self.msg_to_new_var_map: Dict[str, str] = {}
        # e.g. msg_0: PutM
        self.new_var_to_msg_map: Dict[str, str] = {}

        # e.g. msg: 1 -> means there exist two variables with the name msg
        self.var_name_cnt: Dict[str, int] = {}

        self.rename_vars_and_msg(transition)

    ####################################################################################################################
    # Operation mutation
    ####################################################################################################################
    @staticmethod
    def cond_operations_var_rename(operations: List[CommonTree], var_name: str, new_var_name: str,
                                   terminal_token_names: List[str] = None):
        if not terminal_token_names:
            terminal_token_names = []
        for ind in range(0, len(operations)):
            operation = operations[ind]
            token_list = toStringList(operation)
            if var_name in token_list:
                operations[ind] = AuxStateHandler.cond_rename_operation(operation,
                                                                        var_name,
                                                                        new_var_name,
                                                                        terminal_token_names)
        return operations

    @staticmethod
    def cond_rename_operation(operation: CommonTree, var_name: str, new_var_name: str,
                              terminal_token_names: List[str]):
        new_operation = copy_tree(operation)
        nodes = AuxStateHandler.cond_extract_nodes(new_operation, terminal_token_names)

        for node in nodes:
            if node.getText() == var_name:
                node.token.text = new_var_name

        return new_operation

    @staticmethod
    def cond_extract_nodes(operation: CommonTree, terminal_token_names: List[str]):
        nodes = [operation]
        if not operation.children:
            return nodes

        for child in operation.children:
            if str(child) in terminal_token_names:
                continue
            tmp_nodes = AuxStateHandler.cond_extract_nodes(child, terminal_token_names)
            if isinstance(tmp_nodes, list):
                nodes += tmp_nodes
            else:
                nodes.append(tmp_nodes)

        return nodes

    @ staticmethod
    def save_rename_var(operations: List[CommonTree],
                        start_operation: CommonTree,
                        var_name: str,
                        new_var_name: str):
        start = 0
        for ind in range(0, len(operations)):
            operation = operations[ind]
            if operation == start_operation:
                start = 1
            elif start == 1:
                # Check for message var_name reassignment
                if operation.getText() == MurphiTokens.tASSIGN:
                    if operation.getChildren()[0].getText() == var_name:
                        return

            # The initial variable assignment has been found
            if start == 1:
                operations[ind] = AuxStateHandler.cond_rename_operation(operation, var_name, new_var_name, [])

    ####################################################################################################################
    # Data dependency handler(remove unnecessary auxiliary states e.g. messages)
    ####################################################################################################################
    def rename_vars_and_msg(self, transition: 'Transition'):
        assert 0, 'UNUSED FUNCTION'
        # determine message variable names
        for ind in range(0, len(transition.operation)):
            # if the message to be sent is message that is to be removed
            operation = transition.operation[ind]

            if operation.getText() == MurphiTokens.tASSIGN and \
                    (operation.getChildren()[-1]).getText() == MurphiTokens.tMSGCSTR:
                tokens = operation.getChildren()
                varname = tokens[0].getText()
                msg_type = (tokens[-1].getChildren())[1].getText()

                if varname in self.var_name_cnt:
                    new_varname = varname + "_" + str(self.var_name_cnt[varname])
                    new_operation = copy_tree(operation)
                    new_operation.children[0].token.text = new_varname
                    transition.operation[ind] = new_operation
                    self.var_name_cnt[varname] += 1
                else:
                    new_varname = varname
                    self.var_name_cnt[varname] = 0

                # Track current var name assignment
                    self.var_to_new_var_map[varname] = new_varname
                # Track message to var name assignment
                    self.msg_to_new_var_map[msg_type] = new_varname
                # Track new var to message mapping
                    self.new_var_to_msg_map[new_varname] = msg_type

            else:
                # Update the message names
                for key in self.var_to_new_var_map:
                    transition.operation[ind] = \
                        self.cond_operations_var_rename([operation], key, self.var_to_new_var_map[key])[0]

                # Update the message names
                for key in self.msg_to_new_var_map:
                    transition.operation[ind] = \
                        self.cond_operations_var_rename([operation], key, self.msg_to_new_var_map[key])[0]

    def remove_dependent_messages(self, transition: 'Transition'):
        pass
