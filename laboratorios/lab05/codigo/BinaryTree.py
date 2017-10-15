from collections import deque
import BinaryTreeNode


class BinaryTree:
    """
    Simple Binary Tree Implementation.
    """

    def __init__(self, node):
        self.root = node
        self.size = 1

    # --- Insertion
    def insert(self, *data):
        """
        Inserts the node in the
        Binary Search Tree. If the
        node is equal to one already
        in the tree, it is not added.

        :param node: The BinaryTreeNode to be inserted.
        :return: Void
        """
        for d in data:
            self.size += 1
            self.root.insert(d)

    # --- Search
    def search(self, data):
        """
        Returns the node whose data
        equals *data*; None otherwise.

        :param data: The value to be searched.
        :return: BinaryTreeNode
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

        node = self.root.search(data)
        if node is not None:

            # Fringe element deletion
            if node.parent is not None and node.left_node is None and node.right_node is None:
                if node.parent.right_node == node:
                    node.parent.right_node = None
                else:
                    node.parent.left_node = None
                self.size -= 1
            # Root deletion
            elif node.parent is None:
                if node.left_node is not None:
                    right_subtree = self.root.right_node
                    node_left_subtree = node.left_node.left_node
                    node_right_subtree = node.left_node.right_node
                    new_root = node.left_node
                    new_root.parent = None
                    self.root = new_root
                    self.root.insert_node(node_left_subtree)
                    self.root.insert_node(node_right_subtree)
                    self.root.insert_node(right_subtree)
                    self.size -= 1
                elif node.right_node is not None:
                    new_root = node.right_node
                    new_root.parent = None
                    self.root = new_root
                    self.size -= 1
            # Middle node deletion
            else:
                node_left_subtree = node.left_node
                node_right_subtree = node.right_node
                node_parent = node.parent
                if node_parent.left_node == node:
                    node.parent.left_node = None
                else:
                    node.parent.right_node = None
                node_parent.insert_node(node_left_subtree)
                node_parent.insert_node(node_right_subtree)
                self.size -= 1

    # --- Size
    def get_size(self):
        return self.size

    def __len__(self):
        return self.size

    # --- Depth
    def get_depth(self):

        return self.root.get_depth()

    # --- Tree traversal
    def dfs_traverse(self):
        """
        Depth First Search tree traversal.
        """
        fringe = [self.root]
        while len(fringe) > 0:
            next_node = fringe.pop()
            print(next_node)

            if next_node.right_node is not None:
                fringe.append(next_node.right_node)

            if next_node.left_node is not None:
                fringe.append(next_node.left_node)

    def bfs_traverse(self):
        """
        Breadth First Search tree traversal.
        """

        fringe = deque([self.root])
        while len(fringe) > 0:
            next_node = fringe.popleft()
            print(next_node)

            if next_node.left_node is not None:
                fringe.append(next_node.left_node)

            if next_node.right_node is not None:
                fringe.append(next_node.right_node)

    def draw_tree(self):
        """
        Returns the code to draw the tree at
        http://webgraphviz.com/

        :return: String
        """

        tree_str = "digraph G {"

        fringe = [self.root]
        spaces_count = 0
        while len(fringe) > 0:
            next_node = fringe.pop()

            if next_node.left_node is not None:
                fringe.append(next_node.left_node)
                tree_str += '\n\"' + str(next_node.data) + '\"' + " -> " + '\"' + str(next_node.left_node.data) + '\"'
            elif next_node.right_node is not None:
                spaces_count += 1
                tree_str += '\n\"' + str(next_node.data) + '\"' + " -> " + '\"' + (" " * spaces_count) + '\"'

            if next_node.right_node is not None:
                fringe.append(next_node.right_node)
                tree_str += '\n\"' + str(next_node.data) + '\"' + " -> " + '\"' + str(next_node.right_node.data) + '\"'
            elif next_node.left_node is not None:
                spaces_count += 1
                tree_str += '\n\"' + str(next_node.data) + '\"' + " -> " + '\"' + (" " * spaces_count) + '\"'

        return tree_str + "\n}"
