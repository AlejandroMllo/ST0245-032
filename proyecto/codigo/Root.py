"""
Proyecto Final

Presentado por: Juan Pablo Vidal
                Alejandro Murillo
"""

import HashTable

class Root(HashTable.HashTable):

    def __init__(self):
        self.name = ""
        super(HashTable.HashTable, self).__init__()

    def set_name(self, n):
        self.name = n

    def add_file(self, key, file):
        self.add(key, file)

    def print_root(self):
        print(self._hash_table)