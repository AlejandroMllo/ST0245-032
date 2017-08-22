# Taller 6
#
# Presentado por:
#       Juan Pablo Vidal C.
#       Alejandro Murillo G.
#

print("Presentado por:\n\tJuan Pablo Vidal C.\n\tAlejandro Murillo G.")

# --- Array List ---------------------------------------------------
class ArrayList:
    """
    Abstract Data Type for Array List.
    """

    def __init__(self):
        """
        Initializes the private attributes:
            :_size: = 0
            :_DEFAULT_CAPACITY: = 10
            :_elements: = Array with size 10

        """
        self._size = 0
        self._DEFAULT_CAPACITY = 10
        self._elements = [] * self._DEFAULT_CAPACITY

    def size(self):
        """
        Returns the list size.

        :return: self._size
        """
        return self._size

    def add(self, element, i = -1):
        """
        Add the element at the ith
        position.
        By Default i = -1; in that case
        the element is appended to the
        ArrayList.

        :param element: Element to be added.
        :param i: Index.
        """
        if i == -1:
            self._elements += [element]
            self._size += 1

        elif i in range(len(self._elements)):
            _oldElements = self._elements
            self._elements = [] * (int(len(_oldElements) * 1.5) if len(_oldElements) > 1000000 else len(_oldElements) * 2)
            self._size += 1
            for oldIndex in range(len(_oldElements)):
                if i == oldIndex:
                    self._elements += [element, _oldElements[oldIndex]]
                else:
                    self._elements += [_oldElements[oldIndex]]

        else:
            raise IndexError("Invalid index.")

    def get(self, i):
        """
        Returns the element at i. i can be
        a negative integer.
        If i is not in the ArrayList range,
        an IndexError is raised.

        :param i: The index of the element
                  to be retrieved.
        """
        if (i in range(len(self._elements))) or (i in range(-1, -len(self._elements), -1)):
            return self._elements[i]
        raise IndexError("Unavailable element at the specified index.")

    def toString(self):
        """
        Returns the string representation of
        the ArrayList.

        :return: String
        """
        return self._elements



# --- Tests ArrayList

print("\n\n--- ArrayList ---")

arrayList1 = ArrayList()
arrayList1.add("a")
arrayList1.add("b")
arrayList1.add("c")
arrayList1.add("d")

print("\narrayList1 =", arrayList1.toString())
print("arrayList1.get(1) =", arrayList1.get(1))

arrayList1.add("z", 2)
print("arrayList1.add(\"z\", 2) =", arrayList1.toString())

print("arrayList1.get(-2) =", arrayList1.get(-2))

arrayList1.add("e")
print("arrayList1.add(\"e\") =", arrayList1.toString())

print("arrayList1.size() =", arrayList1.size())


# --- Backwards Reading ---------------------------------------------

def readBackwards():
    """
    Reads the elements of an ArrayList.
    When the user inputs "-1" the algorithm
    stops.

    :return: An ArrayList with the elements
             reversed.
    """
    _elements = []
    token = input("Start writing the elements:\n")
    while (token != "-1"):
        _elements.append(token)
        token = input()

    arrayList = ArrayList()
    for i in range(len(_elements) - 1, -1, -1):
        arrayList.add(_elements[i])

    return arrayList


print("\n\n--- Backwards Reading ---")
print(readBackwards().toString())


# --- ArrayList with Increasing Elements -----------------------------

def increasingElements():
    """
    Reads n and returns an ArrayList with
    elements ordered in the following way:
    [1, 1, 2, 1, 2, 3, ..., 1, 2 ... n]

    :return: ArrayList
    """
    numberOfElements = int(input("Number of elements: "))
    _elements = []
    for i in range(1, numberOfElements + 1):
        _elements.append(i)

    arrayList = ArrayList()
    for i in range(int(numberOfElements) + 1):
        for j in range(i):
            arrayList.add(_elements[j])

    return arrayList

print("\n\n--- Increasing Elements ---")
print(increasingElements().toString())