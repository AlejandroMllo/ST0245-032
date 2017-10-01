"""
Proyecto Final

Presentado por: Juan Pablo Vidal
                Alejandro Murillo
"""

class File:

    def __init__(self, name, size, owner):
        name_pieces = name.split(".")
        self.name = name
        self.type = name_pieces[1] if len(name_pieces) > 1 else None
        self.size = size
        self.owner = owner

    # --- Setters
    def set_name(self, name):
        self.name = name

    def set_size(self, size):
        self.size = size

    def set_owner(self, owner):
        self.owner

    # --- Getters
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_size(self):
        return self.size

    def get_owner(self):
        return self.owner

    def __str__(self):
        return "[" + str(self.get_owner()) + " " + str(self.get_size()) + "] " + str(self.get_name())