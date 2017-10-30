"""
Final Project.
Data Structures and Algorithms I.

:authors: Juan Pablo Vidal
          Alejandro Murillo

:date: 10/28/2017
"""

import SearchSpace
import Directory
import File


class Parser:
    """
    Parses the file which describes
    the search space.
    """

    def __init__(self, file_path):
        """
        Initializes the Parser class.
        :param file_path: The path in the system to get the file
                          to be parsed.
        """
        with open(file_path, "r", encoding="utf-8-sig") as file:
            self.text_file = file.read()

    def parse(self):
        """
        Parses the file and returns a SearchSpace
        object which contains the new search space.
        :return: SearchSpace object.
        """
        search_space = SearchSpace.SearchSpace()

        self.text_file = self.text_file.split("\n")
        current_path = self.text_file[0]

        root = Directory.Directory(current_path, "")
        search_space.add(root)

        current_parent_dir_level = 4
        parent_directories = {current_parent_dir_level: root}
        parents_path = {0: current_path}

        for line_index, line in enumerate(self.text_file):

            if line == "\n" or line == "":
                break
            if line_index == 0:
                continue

            level = self.___get_line_hierarchy_level(line)
            file_pieces = line[level:].split()
            size = file_pieces[1][:-1]
            name = " ".join(file_pieces[2:])

            parents_path[level] = str(name) + "/"
            path = ""
            for hierarchy_index in sorted(parents_path.keys()):
                if hierarchy_index > level:
                    break
                path += parents_path[hierarchy_index]

            if line_index + 1 < len(self.text_file):

                next_line_hierarchical_level = self.___get_line_hierarchy_level(self.text_file[line_index + 1])

                if next_line_hierarchical_level > level:
                    archive = Directory.Directory(path, size)
                    parent_directories[current_parent_dir_level].add(archive)
                    current_parent_dir_level = next_line_hierarchical_level
                    parent_directories[current_parent_dir_level] = archive
                    search_space.add(archive)
                elif next_line_hierarchical_level == level:
                    archive = File.File(path, size)
                    parent_directories[current_parent_dir_level].add(archive)
                    search_space.add(archive)
                else:
                    archive = File.File(path, size)
                    parent_directories[current_parent_dir_level].add(archive)
                    search_space.add(archive)
                    current_parent_dir_level = next_line_hierarchical_level
            else:
                archive = File.File(path, size)
                parent_directories[current_parent_dir_level].add(archive)
                search_space.add(archive)

        return search_space

    def ___get_line_hierarchy_level(self, line):
        """
        Returns the hierarchical level of a line.
        :param line: The line to be inspected.
        :return: Integer.
        """
        level = 0
        for character in line:
            if character == "[":
                return level
            else:
                level += 1
        return -1
