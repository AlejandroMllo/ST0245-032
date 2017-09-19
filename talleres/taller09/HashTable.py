# Taller 9
#
# Presentado por:
#       Juan Pablo Vidal C.
#       Alejandro Murillo G.
#

print("Presentado por:\n\tJuan Pablo Vidal C.\n\tAlejandro Murillo G.")


# --- Hash Table ----------------------------------------------
class HashTable:
    """
    Implementation of a simple Hash Table.
    """

    _hash_table = dict()
    _reversed_table = dict()

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
           self._hash_table[htKey] = set()
        self._hash_table[htKey].add(value)
        self._reversed_table[value] = key

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
        return "ERROR: Element not found."

    def search_values(self, value):
        """
        Returns, if it exists, the key associated
        with a value in the hash table.

        :param value: A value on the hash table.
        :return:
        """
        if value in self._reversed_table.keys():
            return self._reversed_table[value]
        return "ERROR: Element not found."

    def get_table(self):
        """
        Returns a copy of the HashTable.

        :return: HashTable
        """
        return self._hash_table

crmHashTable = HashTable()

# --- Punto 3
crmHashTable.add("Google", "Estados Unidos")
crmHashTable.add("La Locura", "Colombia")
crmHashTable.add("Nokia", "Finlandia")
crmHashTable.add("Sony", "Japon")

# --- Punto 4
print("\n\n--------------------\nPunto 4:")
print("Google esta en:", crmHashTable.get("Google"))
print("Motorola esta en:", crmHashTable.get("Motorola"))

# --- Punto 5
print("--------------------\nPunto 5:")
print("En Estados Unidos esta:", crmHashTable.search_values("Estados Unidos"))
