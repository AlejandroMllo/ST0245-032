"""
Final Project.
Data Structures and Algorithms I.

:authors: Juan Pablo Vidal
          Alejandro Murillo

:date: 10/28/2017
"""

import Parser
import Directory

file_path = "D:\AlejandroData\DocumentsData\\Universidad\Semestre 2\Estructuras de Datos y Algoritmos 1\Proyecto Final\Project\Juegos.txt"
file = Parser.Parser(file_path)
search_space = file.parse()


def expand_directory(directory):
    element = directory.get_contents().head
    while element is not None:
        list_dir = input("\t\tDo you want to expand the directory? (1 = Yes / 0 = No): ")
        if list_dir == '1':
            while element is not None:
                print("\t\t   ", element)
                if type(element.get_data()) is Directory.Directory:
                    expand_directory(element.get_data())
                element = element.next
        else:
            break

while True:
    query = input("What are you looking for? ")
    if query.startswith("."):
        query = query[1:]
    answer = search_space.get(query)
    if answer is not None:
        current_node = answer.head
        while current_node is not None:
            print("\t", str(current_node))
            if type(current_node.get_data()) is Directory.Directory:
                expand_directory(current_node.get_data())
                current_node = current_node.next
            current_node = current_node.next
    else:
        print("\tNothing was found.")
