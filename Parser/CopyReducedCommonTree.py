from antlr3.tree import CommonTree, Token


def copy_tree(node: CommonTree) -> CommonTree:
    parent = node.parent
    base_node = copy_node(node)
    base_node.parent = parent
    return base_node


def copy_node(node: CommonTree) -> CommonTree:
    token_str = node.text
    if not token_str:
        token_str = ""
    new_token = Token(text=token_str)
    new_token.TOKEN_NAMES_MAP = None
    new_tree_node = CommonTree(new_token)
    for child in node.children:
        new_tree_node.addChild(copy_node(child))
    return new_tree_node

