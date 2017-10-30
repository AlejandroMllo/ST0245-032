"""
Final Project.
Data Structures and Algorithms I.

:authors: Juan Pablo Vidal
          Alejandro Murillo

:date: 10/28/2017
"""

import LinkedList


class SearchSpace:

    def __init__(self):
        """
        Initializes the SearchSpace.
        """
        self.__data = dict()

    def add(self, archive):
        """
        Saves a File/Directory in the search space.
        :param archive: File/Directory
        :return: Void
        """

        components = archive.get_id_components()
        for component in components:
            if component not in self.__data:
                self.__data[component] = LinkedList.LinkedList()
            self.__data[component].add(archive)

    def get(self, query):
        """
        Returns the elements associated with
        the query key, None otherwise.
        :param query: Identifier of the element to
                      be searched.
        :return: LinkedList.
        """
        return self.__data.get(query)
