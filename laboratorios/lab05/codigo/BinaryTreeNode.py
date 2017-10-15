class BinaryTreeNode:
    """
    Binary Tree Node Implementation.
    """

    def __init__(self, data, left_node=None, right_node=None, parent=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node
        self.parent = parent

    def comparison_value(self):
        """
        The value to be used while
        sorting the nodes in the tree.
        :return: Number
        """
        return self.data

    def set_parent(self, parent):
        self.parent = parent

    def insert(self, *nodes):

        if self is None or nodes is None:
            return

        for node in nodes:

            if self.comparison_value() < node.comparison_value():
                if self.right_node is None:
                    self.right_node = node
                    node.set_parent(self)
                else:
                    self.right_node.insert_node(node)
            elif self.comparison_value() > node.comparison_value():
                if self.left_node is None:
                    self.left_node = node
                    node.set_parent(self)
                else:
                    self.left_node.insert_node(node)

    def insert_node(self, node):

        if self is None or node is None:
            return

        if self.comparison_value() < node.comparison_value():
            if self.right_node is None:
                node.parent = self.right_node.parent if self.right_node is not None else None
                self.right_node = node
                node.set_parent(self)
            else:
                self.right_node.insert_node(node)
        elif self.comparison_value() > node.comparison_value():
            if self.left_node is None:
                node.parent = self.left_node.parent if self.left_node is not None else None
                self.left_node = node
                node.set_parent(self)
            else:
                self.left_node.insert_node(node)

    def search(self, data):

        if self is None or data is None:
            return

        if self.comparison_value() < data:
            return self.right_node.search(data) if self.right_node is not None else None
        elif self.comparison_value() > data:
            return self.left_node.search(data) if self.left_node is not None else None
        else:
            return self

    def get_depth(self):

        if self.left_node is None and self.right_node is None:
            return 1

        left_depth = right_depth = 0
        if self.left_node is not None:
            left_depth = 1 + self.left_node.get_depth()
        if self.right_node is not None:
            right_depth = 1 + self.right_node.get_depth()

        return max(left_depth, right_depth)

    def str_with_parents(self):
        "[" + str(self.data) + " Parent = " + str(self.parent) + "]"

    def __str__(self):
        return str(self.data)
