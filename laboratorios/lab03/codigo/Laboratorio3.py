# Laboratorio 3
#
# Presentado por:
#       Juan Pablo Vidal C.
#       Alejandro Murillo G.
#

print("Presentado por:\n\tJuan Pablo Vidal C.\n\tAlejandro Murillo G.")

import LinkedList
import ArrayList

class Laboratorio3:

    def __init__(self):

        # --- Linked List ---
        linked_list = LinkedList.LinkedList()
        linked_list.add(4)
        linked_list.add(5)
        linked_list.add_at_start(10)
        linked_list.add(3)

        # Multiplication
        multiplication_linked_list = self.element_multiplication_linked_list(linked_list)

        # Smart Insert
        self.smart_insert(linked_list, 10)
        self.smart_insert(linked_list, 6)

        # --- Array List ---
        array_list = ArrayList.ArrayList()
        array_list.add(4)
        array_list.add(5)
        array_list.add(20, 1)
        array_list.add(4, 2)
        array_list.add(1)

        # Multiplication
        multiplication_array_list = self.element_multiplication_array_list(array_list)

        # Smart Insert
        self.smart_insert(array_list, 5)
        self.smart_insert(array_list, 14)

        # --- Ejercicio 4
        almacen = [(1, "haceb"), (2, "lg"), (3, "ibm"), (4, "haceb"),
                   (5, "lg"), (6, "ibm"), (7, "haceb"), (8, "lg"),
                   (9, "ibm"), (8, "lg"), (9, "ibm")]
        solicitudes = [("eafit", 10), ("la14", 2), ("olimpica", 4),
                             ("exito", 1)]

        print("\n\n", self.ejercicio_4(almacen, solicitudes))

    # --- Element Multiplication
    def element_multiplication_linked_list(self, list):

        current = list.head
        multiplication = current.data
        while current.next != None:
            current = current.next
            multiplication *= current.data

        return multiplication

    def element_multiplication_array_list(self, list):

        multiplication = 1
        for i in range(list.size()):
            multiplication *= list.get(i)

        return multiplication

    # --- Smart Insert: Inserts non-repeated elements on the list
    def smart_insert(self, list, element):
        if element not in list:
            list.add(element)

    # --- Pivot element
    def pivot_element(self, list):
        """
        Returns the position of the element that makes the list's elements sum
        as balanced as possible to its left and its right.

        :param list:
        :return: Pivot element's index
        """
        leftSum = rightSum = 0

    # --- Refrigerator Factory
    def ejercicio_4(self, almacen, solicitudes):
        ordenes = []
        while len(almacen) > 0 and len(solicitudes) > 0:
            tienda, numero_neveras_solicitadas = solicitudes.pop()
            neveras_entregadas = []
            for _ in range(numero_neveras_solicitadas):
                if len(almacen) > 0:
                    neveras_entregadas.append(almacen.pop())
            ordenes.append((tienda, neveras_entregadas))

        return ordenes

Laboratorio3()
