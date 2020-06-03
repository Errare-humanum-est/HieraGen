from antlr3.tree import CommonTree


class ClassNetwork:

    ordered = "Ordered"
    unordered = "Unordered"

    def __init__(self, network_node: CommonTree):
        self.network_name: str = str(network_node.children[1])
        self.network_type: str = str(network_node.children[0])

        assert self.network_type == self.ordered or self.network_type == self.unordered, "Unrecognized network type"

    def __str__(self):
        return self.network_name
