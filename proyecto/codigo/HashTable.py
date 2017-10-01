"""
Proyecto Final

Presentado por: Juan Pablo Vidal
                Alejandro Murillo
"""
class HashTable:
    """
    Implementation of a simple Hash Table.
    """

    _hash_table = dict()

    def _hash_function(self, key):
        """
        Computes a simple hash function for a
        given key.
        :param key: The key to be hashed.
        :return: String
        """
        computation = ""
        for c in key:
            computation += str(ord(c) ** 2)
        return computation

    def add(self, key, value):
        """
        Adds a new element to the hash table.

        :param key: The element's key.
        :param value: The element's value.
        :return: Void
        """
        if value == None:
            value = key
        htKey = self._hash_function(key)
        if htKey not in self._hash_table:
           self._hash_table[htKey] = list()
        self._hash_table[htKey] += [value]

    def get(self, key):
        """
        Returns, if it exists, the value associated
        with the given key in the hash table.

        :param key: The key of the element to be retrieved.
        :return:
        """
        htKey = self._hash_function(key)
        if htKey in self._hash_table.keys():
            return self._hash_table[htKey]
        raise KeyError("ERROR: Element not found.")

    def get_table(self):
        """
        Returns a copy of the HashTable.

        :return: HashTable
        """
        return self._hash_table