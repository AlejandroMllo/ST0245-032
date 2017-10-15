import BinaryTreeNode


class PersonNode(BinaryTreeNode.BinaryTreeNode):
    """
    This class enables us to have a
    numerical representation of a person
    in order to correctly arrange it
    on a Binary Tree.
    """

    def __init__(self, name, value):
        BinaryTreeNode.BinaryTreeNode.__init__(self, name)
        self.value = value

    def comparison_value(self):
        return float(self.value)

    def search(self, data):

        if isinstance(data, float):
            return super.search(data)
        else:
            fringe = [self]
            while len(fringe) > 0:
                next_node = fringe.pop()

                if next_node.data == data:
                    return next_node

                if next_node.right_node is not None:
                    fringe.append(next_node.right_node)

                if next_node.left_node is not None:
                    fringe.append(next_node.left_node)

        return None

    def __str__(self):
        return str(self.data)