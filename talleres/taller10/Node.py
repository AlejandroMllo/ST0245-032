# Taller 10
#
# Presentado por:
#       Juan Pablo Vidal C.
#       Alejandro Murillo G.
#

class Node:
    """
    Binary Tree Node Implementation.
    """

    def __init__(self, data, left_node = None, right_node = None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

    # --- Getters
    def get_data(self):
        return self.data

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

    def __str__(self):
        return str(self.data)

