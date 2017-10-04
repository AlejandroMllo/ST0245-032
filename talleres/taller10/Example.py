# Taller 10
#
# Presentado por:
#       Juan Pablo Vidal C.
#       Alejandro Murillo G.
#

import Node
import BinaryTree

#Left Subtree
florinda = Node.Node("Florinda")
eustaquia = Node.Node("Eustaquia", florinda)
jovin = Node.Node("Jovin")
eustaquio = Node.Node("Eustaquio", right_node = jovin)
joaquina = Node.Node("Joaquina", eustaquia, eustaquio)

#Right Subtree
wilberta = Node.Node("Wilberta")
piolina = Node.Node("Piolina", wilberta)
usnavy = Node.Node("Usnavy")
piolin = Node.Node("Piolin", right_node = usnavy)
sufranio = Node.Node("Sufranio", piolina, piolin)

#Root
root = Node.Node("Wilkenson", joaquina, sufranio)

tree = BinaryTree.BinaryTree(root)

# --- BFS Tree traversal
print("\n--- BFS Tree traversal ---")
tree.bfs_traverse()

# --- DFS Tree traversal
print("\n--- DFS Tree traversal ---")
tree.dfs_traverse()

# --- Drawing Tree
print("\n--- Drawn tree at: http://webgraphviz.com/ ---")
print(tree.draw_tree())
