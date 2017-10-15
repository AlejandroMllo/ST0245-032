import BinaryTree
import PersonNode


class FamilyTree(BinaryTree.BinaryTree):
    """
    Binary tree of a family's
    ancestors tree.
    """

    def __init__(self, name, value):
        person = PersonNode.PersonNode(name, value)
        BinaryTree.BinaryTree.__init__(self, person)

    def insert(self, name, value):
        node = PersonNode.PersonNode(name, value)
        super(FamilyTree, self).insert(node)

    def get_grandmother(self, name):
        person = self.root.search(name)

        if person.left_node is not None and person.left_node.left_node is not None:
            return person.left_node.left_node
        return "Unknown"

# --- Family Tree --------------------------------
tree = FamilyTree("Wilkenson", 100)

# Left subtree
tree.insert("Joaquina", 50)
tree.insert("Eustaquia", 25)
tree.insert("Florinda", 10)
tree.insert("Eustaquio", 75)
tree.insert("Jovin", 90)

# Right subtree
tree.insert("Sufranio", 150)
tree.insert("Piolina", 125)
tree.insert("Wilberta", 110)
tree.insert("Piolin", 175)
tree.insert("Usnavy", 190)

# --- Tests
print("Wilkenson's grandmother:", tree.get_grandmother("Wilkenson"))
print("Eustaquia's grandmother:", tree.get_grandmother("Eustaquia"))

print(tree.draw_tree())
print("Depth:", tree.get_depth())
print("Size:", tree.get_size())

tree.delete("Wilkenson")
print(tree.draw_tree())
print("Depth:", tree.get_depth())
print("Size:", tree.get_size())

print("Sufranio's grandmother:", tree.get_grandmother("Sufranio"))

tree.delete("Wilberta")
print(tree.draw_tree())
print("Depth:", tree.get_depth())
print("Size:", tree.get_size())

tree.delete("Wk")
print(tree.draw_tree())
print("Depth:", tree.get_depth())
print("Size:", tree.get_size())

tree.delete("Jovin")
print(tree.draw_tree())
print("Depth:", tree.get_depth())
print("Size:", tree.get_size())