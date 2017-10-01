"""
Proyecto Final

Presentado por: Juan Pablo Vidal
                Alejandro Murillo
"""

import TreeParser

file = TreeParser.TreeParser("D:\AlejandroData\DocumentsData\\Universidad\Semestre 2\Estructuras de Datos y Algoritmos 2\Proyecto Final\Project\ShortTree.txt")
parsed_file = file.parse()

while 1:
    query = input("What are you looking for? ")
    try:
        for e in parsed_file.get(query):
            print("\t", e)
    except:
        print("\tNothing was found.")