class ArrayList:
    """
    Abstract Data Type for Array List.
    @Author: Juan Pablo Vidal C.
             Alejandro Murillo G.
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

    def __str__(self):
        """
        Returns the string representation of
        the ArrayList.
        :return: String
        """
        return str(self._elements)

    def __contains__(self, item):
        return item in self._elements
