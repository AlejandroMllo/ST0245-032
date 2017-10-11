# Taller 11
#
# Presentado por:
#       Juan Pablo Vidal C.
#       Alejandro Murillo G.
#

from collections import deque

class BinaryTree:
    """
    Simple Binary Tree Implementation.
    """

    class Node:
        """
        Binary Tree Node Implementation.
        """

        def __init__(self, data, left_node = None, right_node = None, parent = None):
            self.data = data
            self.left_node = left_node
            self.right_node = right_node
            self.parent = parent

        def insert(self, data):

            if self.data < data:
                if self.right_node == None:
                    self.right_node = BinaryTree.Node(data, parent=self)
                else:
                    self.right_node.insert(data)
            elif self.data > data:
                if self.left_node == None:
                    self.left_node = BinaryTree.Node(data, parent=self)
                else:
                    self.left_node.insert(data)

        def insert_node(self, node):

            if self.data < node.data:
                if self.right_node == None:
                    print('Inserted node', str(node), " to " + str(self))
                    node.parent = self.right_node.parent if self.right_node != None else None
                    self.right_node = node
                else:
                    self.right_node.insert_node(node)
            elif self.data > node.data:
                if self.left_node == None:
                    print('Inserted node', str(node), " to " + str(self))
                    node.parent = self.left_node.parent if self.left_node != None else None
                    self.left_node = node

                else:
                    self.left_node.insert_node(node)


        def search(self, data):

            if self.data < data:
                return self.right_node.search(data) if self.right_node != None else None
            elif self.data > data:
                return self.left_node.search(data) if self.left_node != None else None
            else:
                return self

        def delete(self, data, tree):

            node = self.search(data)
            if node != None:

                #Fringe element deletion
                if node.parent != None and node.left_node == node.right_node == None:
                    if node.parent.right_node == node:
                        node.parent.right_node = None
                    else:
                        node.parent.left_node = None
                #Root deletion
                elif node.parent == None:
                    if node.left_node != None:
                        node.left_node.insert_node(node.right_node)
                        node.left_node.right_node = tree.root.right_node
                        tree.root = node.left_node
                    elif node.right_node != None:
                        node.right_node.insert_node(node.left_node)
                        node.right_node.left_node = tree.root.left_node
                        tree.root = node.right_node

                elif node.left_node != None:
                    node.left_node.parent = node.parent
                    node.parent.left_node = node.left_node
                    node.right_node.parent = node.left_node
                elif node.right_node != None:
                    node.right_node.parent = node.parent
                    node.parent.right_node = node.right_node
                    node.left_node.parent = node.right_node

        def __str__(self):
            return str(self.data)


    def __init__(self, data):
        self.root = BinaryTree.Node(data)

    # --- Insertion
    def insert(self, data):
        """
        Inserts the node in the
        Binary Search Tree. If the
        node is equal to one already
        in the tree, it is not added.

        :param node: The Node to be inserted.
        :return: Void
        """
        self.root.insert(data)


    # --- Search
    def search(self, data):
        """
        Returns the node whose data
        equals *data*; None otherwise.

        :param data: The value to be searched.
        :return: Node
        """
        return self.root.search(data)

    # --- Deletion
    def delete(self, data):
        """
        Deletes the node whose data
        equals *data*.

        :param data: The node's data.
        :return: Void
        """
        self.root.delete(data, self)


    # --- Tree traversal
    def dfs_traverse(self):
        """
        Depth First Search tree traversal.
        """

        fringe = [self.root]
        while len(fringe) > 0:
            next_node = fringe.pop()
            print(next_node)

            if next_node.right_node != None:
                fringe.append(next_node.right_node)

            if next_node.left_node != None:
                fringe.append(next_node.left_node)


    def bfs_traverse(self):
        """
        Breadth First Search tree traversal.
        """

        fringe = deque([self.root])
        while len(fringe) > 0:
            next_node = fringe.popleft()
            print(next_node)

            if next_node.left_node != None:
                fringe.append(next_node.left_node)

            if next_node.right_node != None:
                fringe.append(next_node.right_node)

    def draw_tree(self):
        """
        Returns the code to draw the tree at
        http://webgraphviz.com/

        :return: String
        """

        tree = "digraph G {"

        fringe = [self.root]
        spaces_count = 0
        while len(fringe) > 0:
            next_node = fringe.pop()

            if next_node.left_node != None:
                fringe.append(next_node.left_node)
                tree += '\n\"' + str(next_node.data) + '\"' + " -> " + '\"' + str(next_node.left_node.data) + '\"'
            elif next_node.right_node != None:
                spaces_count += 1
                tree += '\n\"' + str(next_node.data) + '\"' + " -> " + '\"' + (" " * spaces_count) + '\"'


            if next_node.right_node != None:
                fringe.append(next_node.right_node)
                tree += '\n\"' + str(next_node.data) + '\"' + " -> " + '\"' + str(next_node.right_node.data) + '\"'
            elif next_node.left_node != None:
                spaces_count += 1
                tree += '\n\"' + str(next_node.data) + '\"' + " -> " + '\"' + (" " * spaces_count) + '\"'

        return tree + "\n}"
