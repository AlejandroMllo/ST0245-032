"""
Final Project.
Data Structures and Algorithms I.

:authors: Juan Pablo Vidal
          Alejandro Murillo

:date: 10/28/2017
"""


class File:
    """
    Represents the structure of a
    file in the search space.
    """

    def __init__(self, path, size):
        """
        Initializes the File class.
        :param path: The path to the file in the
                     directory.
        :param size: The file's size.
        """
        self.__path = str(path)
        self.__size = str(size)

    def get_id_components(self):
        """
        Returns a List with the string
        components that distinguish this
        File.
        :return: List of identifiers.
        """
        return [self.get_path(), self.get_size(), self.get_name(), self.get_short_name(), self.get_type()]

    # --- Setters
    def set_size(self, size):
        """
        Changes the file's size.
        :param size: The new size.
        :return: Void.
        """
        self.__size = size

    # --- Getters
    def get_path(self):
        """
        Returns the file's path.
        :return: String.
        """
        return self.__path

    def get_name(self):
        """
        Returns the full name of the file.
        :return: String.
        """
        return self.__path.split("/")[-2]

    def get_short_name(self):
        """
        Returns the name of the file, without
        its type.
        :return: String.
        """
        name_pieces = self.__path.split("/")[-2].split(".")[:-1]
        if len(name_pieces) > 1:
            name_pieces = ".".join(name_pieces)
        return "".join(name_pieces)

    def get_type(self):
        """
        Returns the file's type.
        :return: String
        """
        return self.__path.split("/")[-2].split(".")[-1]

    def get_size(self):
        """
        Returns the file's size.
        :return: String.
        """
        return self.__size

    def __str__(self):
        """
        String representation of the file.
        :return: String.
        """
        return "[" + str(self.get_size()) + "] " + str(self.get_name())
