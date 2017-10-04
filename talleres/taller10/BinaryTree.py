# Taller 10
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

    def __init__(self, root):
        self.root = root

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
                tree += '\n\"' + next_node.data + '\"' + " -> " + '\"' + next_node.left_node.data + '\"'
            elif next_node.right_node != None:
                spaces_count += 1
                tree += '\n\"' + next_node.data + '\"' + " -> " + '\"' + (" " * spaces_count) + '\"'


            if next_node.right_node != None:
                fringe.append(next_node.right_node)
                tree += '\n\"' + next_node.data + '\"' + " -> " + '\"' + next_node.right_node.data + '\"'
            elif next_node.left_node != None:
                spaces_count += 1
                tree += '\n\"' + next_node.data + '\"' + " -> " + '\"' + (" " * spaces_count) + '\"'

        return tree + "\n}"
