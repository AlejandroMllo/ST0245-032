import BinaryTree
import BinaryTreeNode
from collections import deque


def preorder_to_postorder():

    node = input()
    tree = BinaryTree.BinaryTree(BinaryTreeNode.BinaryTreeNode(int(node)))
    while node != "":
        tree.insert(BinaryTreeNode.BinaryTreeNode(int(node)))
        node = input()

    fringe = deque([tree.root])
    postorder = deque([])
    while len(fringe) > 0:
        next_node = fringe.popleft()
        postorder.appendleft(next_node)

        if next_node.left_node is not None:
            fringe.appendleft(next_node.left_node)

        if next_node.right_node is not None:
            fringe.appendleft(next_node.right_node)

    for node in postorder:
        print(node)


preorder_to_postorder()
