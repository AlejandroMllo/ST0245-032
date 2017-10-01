"""
Proyecto Final

Presentado por: Juan Pablo Vidal
                Alejandro Murillo
"""

import LinkedList

class Directory(LinkedList.LinkedList):

    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        super(LinkedList.LinkedList, self).__init__()

    def add_file(self, file):
        self.add(file)

    # --- Getters
    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def get_parent(self):
        return self.parent