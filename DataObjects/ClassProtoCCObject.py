from typing import Dict

from antlr3.tree import CommonTree
from Parser.ProtoCCParser import ProtoCCParser
from Parser.ProtoCCcomTreeFct import *
from Monitor.ClassDebug import Debug


class PCCObject:
    def __init__(self, node, debug_enable: bool = False):

        dbg = Debug(debug_enable)
        assert isinstance(node, CommonTree)

        self.structure = node

        definitions = node.getChildren()
        self.name = definitions[0].getText()
        self.variables = {}
        self.getvarnames(definitions)
        dbg.pdebug("Object: " + node.getText() + " " + self.name + " -> varNames: " + str(self.variables))

    def __str__(self):
        return self.name

    def getvarnames(self, nodes):
        self.variables = {}
        assign = 'INITVAL_'
        for node in nodes:
            # Check if data type
            if node.getText() in ProtoCCParser.tokenNames:
                entry = toStringList(node)
                if assign in entry:
                    self.variables.update({entry[entry.index(assign)-1]: node.getText()})
                else:
                    self.variables.update({entry[-1]: node.getText()})

    def get_var_object_dict(self) -> Dict[str, CommonTree]:
        nodes = self.structure.getChildren()
        var_obj_dict = {}
        assign = 'INITVAL_'
        for node in nodes:
            # Check if data type
            if node.getText() in ProtoCCParser.tokenNames:
                entry = toStringList(node)
                if assign in entry:
                    var_obj_dict.update({entry[entry.index(assign) - 1]: node})
                else:
                    var_obj_dict.update({entry[-1]: node})
        return var_obj_dict

    def getname(self):
        return self.name

    def getvariables(self):
        return self.variables

    def testname(self, name):
        if name == self.name:
            return 1
        return 0

    def testvariable(self, name):
        if name in self.variables:
            return 1
        return 0

    def getnode(self):
        return self.structure
