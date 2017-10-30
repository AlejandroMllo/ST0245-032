class LinkedList:
    """
    Implementation of a simple
    LinkedList.
    @Author: Alejandro Murillo
    """

    class Node:
        """
        Implementation of the
        LinkedList's node.
        """

        def __init__(self, data):
            """
            Creates a new Node.
            :param data: The node's data.
            """
            self.data = data
            self.next = None
            self.previous = None

        def get_data(self):
            return self.data

        def __str__(self):
            return str(self.data)

    def __init__(self):
        """
        Creates a new LinkedList.
        Initializes the Head and Tail node
        to None; and its size to 0.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def add_at_start(self, data):
        """
        Adds an element at the start of the
        LinkedList.
        :param data: The new Node data.
        :return: Void
        """

        new_node = self.Node(data)

        if self.head is not None:
            self.head.previous = new_node
            new_node.next = self.head

        self.head = new_node
        self.size += 1

        if self.size == 1:
            self.tail = self.head

    def add(self, data):
        """
        Adds an element to the end of
        the list.
        :param data: The new Node data.
        :return: Void
        """

        if self.head is None:
            self.add_at_start(data)
        else:
            new_node = self.Node(data)
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

    def delete_end(self):
        """
        Deletes the last element on the
        LinkedList.
        :return: Void
        """
        self.tail = self.tail.previous
        self.tail.next = None
        self.size -= 1

    def delete_start(self):
        """
        Deletes the first element
        on the LinkedList.
        :return: Void
        """
        self.head = self.head.next
        self.head.previous = None
        self.size -= 1

    def get(self, i):
        """
        Returns the ith linked element.
        :param i: Element's index.
        :return: Node
        """

        if i >= self.size or i < 0:
            return IndexError("Unavailable element at the specified index.")

        if self.head is not None:
            return None

        iteration = 0
        current = self.head

        while iteration != i and current.next is not None:
            current = current.next
            iteration += 1

        return current

    def print_reversed(self):
        """
        Prints the list in reverse order.
        :return: Void
        """
        current = self.tail
        s = str(current.data)
        while current.previous is not None:
            current = current.previous
            s += ", " + str(current.data)

        print(s)

    def __str__(self):
        if self.head is None:
            return "[]"
        current = self.head
        s = "[" + str(current.data)
        while current.next is not None:
            current = current.next
            s += ", " + str(current.data)

        return s + "]"

    def __contains__(self, item):

        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def __len__(self):
        return self.size
