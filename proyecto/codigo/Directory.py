"""
Final Project.
Data Structures and Algorithms I.

:authors: Juan Pablo Vidal
          Alejandro Murillo

:date: 10/28/2017
"""

import LinkedList


class Directory:
    """
    Represents the structure of a
    directory in the search space.
    """

    def __init__(self, path, size):
        """
        Initializes the Directory class.
        :param path: The path to this directory in the
                     search space.
        :param size: Directory's size (String).
        """
        self.__path = path
        self.__size = size
        self.__contents = LinkedList.LinkedList()

    def add(self, archive):
        """
        Adds archive to the contents hierarchy
        of the Directory.
        :param archive: File/Directory.
        :return: Void
        """
        self.__contents.add(archive)

    # --- Getters
    def get_id_components(self):
        """
        Returns a List with the string
        components that distinguish this
        Directory.

        :return: List of string.
        """
        return [self.get_path(), self.get_size(), self.get_name(), self.get_type()]

    def get_contents(self):
        """
        Returns a LinkedList that represents
        the hierarchy and contains the archives
        inside the directory.
        :return: LinkedList
        """
        return self.__contents

    def get_path(self):
        """
        Returns the directory's path.
        :return: String.
        """
        return self.__path

    def get_name(self):
        """
        Returns the name of the directory.
        :return: String.
        """
        return self.__path.split("/")[-2]

    def get_type(self):
        """
        Returns the directory's type.
        :return: String
        """
        return self.__path.split("/")[-2].split(".")[-1]

    def get_size(self):
        """
        Returns the directory's size.
        :return: String.
        """
        return self.__size

    def __str__(self):
        """
        String representation of the directory.
        :return: String.
        """
        return "[" + str(self.get_size()) + "] " + str(self.get_name())
