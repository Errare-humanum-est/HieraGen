from typing import List, Any, Union

class Node:
    def __init__(self, predecessor, data):
        self.predecessor = predecessor
        self.data = data
        self.successor = []

    def __str__(self):
        return str(self.data)

    def getpredecessor(self):
        return self.predecessor

    def setpredecessor(self, predecessor):
        self.predecessor = predecessor
        return predecessor

    def addsuccessor(self, successor):
        if isinstance(successor, Node):
            self.successor.append(successor)
            return 1
        return 0

    def getsuccessors(self) -> List['Node']:
        return self.successor

    def testsuccessor(self):
        if self.successor:
            return 1
        return 0

    def removesuccessor(self, successor):
        if self.successor:
            return self.successor.remove(successor)
        else:
            return 0

    def getdata(self):
        return self.data


class ForkTree:

    def __init__(self):
        self.Tree: List[Node] = []
        self.curNode: Node = None

    def gettreenodecontent(self):
        ret = []
        for node in self.Tree:
            ret.append(node.getdata())
        return ret

    def getcurnode(self):
        return self.curNode

    def getcurnodepre(self):
        if self.curNode:
            return self.curNode.getpredecessor()
        return None

    def set_cur_node(self, node: Node):
        self.curNode = node

    # Transaction legacy
    def getbasenode(self):
        for indsel in range(0, len(self.Tree)):
            found = 0
            predecessor = self.Tree[indsel].getpredecessor()
            for indent in range(0, len(self.Tree)):
                if indsel != indent and predecessor == self.Tree[indent]:
                    found = 1
                    break

            if not found:
                return predecessor
        return 0

    def get_base_node(self) -> [Node, None]:
        for node in self.Tree:
            if not node.getpredecessor():
                return node
        return None

    def popcurnode(self):
        self.curNode = self.getcurnodepre()
        return self.curNode

    def popdelcurnode(self, curnode):
        prenode = self.popcurnode()
        self.Tree.remove(curnode)
        if prenode:
            prenode.removesuccessor(curnode)
        return prenode

    def insertnode(self, data: Any, prenode: Node = None):
        if not prenode:
            node = self.curNode
        else:
            node = prenode

        newnode = Node(node, data)
        self.Tree.append(newnode)

        if node and self.curNode:
            self.curNode.addsuccessor(newnode)

        self.curNode = newnode

        return newnode

    def appendnodes(self, nodes: List[Node], predecessor: Node):
        if predecessor and predecessor not in self.Tree:
            return 0
        for entry in nodes:
            entry.setpredecessor(predecessor)
            self.Tree.append(entry)
            if predecessor:
                predecessor.addsuccessor(entry)
            self.curNode = entry
        return self.curNode

    def appenddata(self, data: List[Any], predecessor: Node):
        nodes = []
        if predecessor and predecessor not in self.Tree:
            return 0
        for entry in data:
            node = Node(predecessor, entry)
            nodes.append(node)
            self.Tree.append(node)
            if predecessor:
                predecessor.addsuccessor(node)

        return nodes

    def append_data_list(self, data: List[Union[Any, List[Any]]], predecessor: Node):
        nodes = []
        if predecessor and predecessor not in self.Tree:
            return 0
        for block in data:
            if not isinstance(block, list):
                nodes += self.appenddata([block], predecessor)
            else:
                cur_predecessor = predecessor
                for entry in block:
                    node = Node(cur_predecessor, entry)
                    nodes.append(node)
                    self.Tree.append(node)
                    if cur_predecessor:
                        cur_predecessor.addsuccessor(node)
                    cur_predecessor = node

        return nodes

    def getpredecessor(self):
        self.curNode = self.curNode.getpredecessor()
        return self.curNode

    def getnodeandchilds(self):
        childs = self.curNode.getsuccessors()
        nodes = [self.curNode]
        while childs:
            newchilds = []
            for entry in childs:
                nodes.append(entry)
                newchilds += entry.getsuccessors()

            childs = newchilds

        return nodes

    def get_nodes(self):
        return self.Tree

    def get_direct_children(self, cur_node: Node = None):
        if cur_node:
            return cur_node.getsuccessors()
        return self.curNode.getsuccessors()

    def getchildnodes(self, curnode):
        children = [curnode]
        successors = curnode.getsuccessors()

        while successors:
            nextsuc = []
            for entry in successors:
                children.append(entry)
                nextsuc += entry.getsuccessors()

            if not nextsuc:
                return children

            successors = nextsuc
        return children

    def getendnodes(self):
        endnodes = []
        for entry in self.Tree:
            if not entry.testsuccessor():
                endnodes.append(entry)

        return endnodes

    def gettraces(self) -> List[List['TraceNodeObj']]:
        traces = []
        endnodes = self.getendnodes()

        for endnode in endnodes:
            node = endnode
            trace = [node.getdata()]

            while node.getpredecessor():
                node = node.getpredecessor()
                trace.append(node.getdata())

            traces.append(trace)

        return traces

    def treetoarray(self):
        # Get end nodes
        endnodes = []
        for entry in self.Tree:
            if entry.testsuccessor():
                endnodes.append(entry)

        ret = []
        for entry in endnodes:
            curcond = []
            curcond += entry.getdata()
            predecessor = entry.getpredecessor()

            # Search backwards for predecessor
            while predecessor:
                curcond += predecessor.getdata()
                predecessor = predecessor.getpredecessor()

            ret.append(curcond)

    # Print all generated transactions
    def treetolist(self):
        ret = []
        for entry in self.Tree:
            ret.append(entry.getdata())

        return ret







