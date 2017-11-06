import LinkedList


class GraphAL:
    """
    Basic implementation of a graph
    whose edges are stored in an
    adjacency list.
    """

    def __init__(self):
        self.vertices = dict()

    def create_from_file(self, file_path):
        with open(file_path, "r", encoding="utf-8-sig") as file:
            text_file = file.read()

        text = text_file.split("\n")

        for token in text:
            if not token.startswith("Vertices") and not token.startswith("Arcos") and not token == "":
                tokens = token.split()
                if tokens[1].find(".") == -1:
                    self.insert_edge(tokens[0], tokens[1])
                else:
                    self.insert_vertex(tokens[0])

    def insert_vertex(self, vertex):
        """
        Inserts a vertex to the graph.
        Raises an AttributeError if the
        vertex is already in the graph.
        :param vertex: The vertex to be inserted.
        :return: Void.
        """
        if vertex not in self.vertices:
            self.vertices[vertex] = LinkedList.LinkedList()
        else:
            raise AttributeError("This vertex is already in the graph.")

    def insert_vertices(self, *vertices):
        """
        Inserts multiple vertices to the graph.
        Raises an AttributeError if a vertex
        is already in the graph.
        :param vertices: The vertices to be inserted.
        :return: Void.
        """
        for vertex in vertices:
            self.insert_vertex(vertex)

    def insert_edge(self, vertex, successor, weight = 0):
        """
        Inserts an edge to the vertex and assigns
        a weight to the connection. If the successor
        vertex is not in the graph, it is added first.
        Raises an error if the vertex is not in the graph.
        :param vertex: The vertex who has the connection.
        :param successor: The vertex's successor vertex.
        :param weight: The connection weight.
        :return: Void.
        """
        if vertex in self.vertices:
            if successor not in self.vertices:
                self.insert_vertex(successor)
            self.vertices[vertex].add((successor, weight))
        else:
            raise AttributeError("This vertex is not in the graph.")

    def get_successors(self, vertex):
        """
        Returns the successor of vertex.
        If vertex does not exist, it raises
        an AttributeError.
        :param vertex: The vertex whose successors are to be retrieved.
        :return: LinkedList of successors.
        """

        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            raise AttributeError("This vertex is not in the graph.")

    def get_vertex_with_more_successors(self):
        """
        Returns the vertex with more
        successors.
        :return: Tuple representation of vertex.
        """

        index_vertex_with_more_successors = None

        for vertex, successors in self.vertices.items():
            if index_vertex_with_more_successors is None:
                index_vertex_with_more_successors = vertex
            elif len(successors) > len(self.vertices[index_vertex_with_more_successors]):
                index_vertex_with_more_successors = vertex

        return index_vertex_with_more_successors, self.vertices[index_vertex_with_more_successors]

    def draw_graph(self):
        """
        Returns the code to draw the graph at
        http://webgraphviz.com/
        :return: String
        """

        graph = "digraph G {"
        for vertex, edges in self.vertices.items():
            current_edge = edges.head
            while current_edge is not None:
                graph += '\n\"' + str(vertex) + '\"' + " -> " + '\"' + str(current_edge.data[0]) + '\"'
                graph += ((" [label = \"" + str(current_edge.data[1]) + "\"] ") if current_edge.data[1] != 0 else "")
                current_edge = current_edge.next
        return graph + "\n}"

    def __str__(self):
        vertices_str = ""
        for vertex, edges in self.vertices.items():
            vertices_str += str(vertex) + " -> " + str(edges) + "\n"

        return vertices_str

# graph = GraphAL()
# graph.insert_vertices(2, 3, 5, 7, 8, 9, 10, 11)
# graph.insert_edge(3, 8)
# graph.insert_edge(3, 10)
# graph.insert_edge(5, 11)
# graph.insert_edge(7, 8)
# graph.insert_edge(7, 11)
# graph.insert_edge(8, 9)
# graph.insert_edge(11, 2)
# graph.insert_edge(11, 9)
# graph.insert_edge(11, 11)
#
# print("--- Adjacency List Graph ---")
# print(graph)
# print("Successors 7: " + str(graph.get_successors(7)) + "\n")
# print(graph.draw_graph())
#
# more_successors = graph.get_vertex_with_more_successors()
# print("\nVertex with more successors:", more_successors[0], "\n\tSuccessors:", more_successors[1])
#
# medellin_graph = GraphAL()
# medellin_graph.create_from_file("/Users/AlejandroMurillo/Desktop/Laboratorio6/medellin_colombia-grande.txt")
#
#
# with open("/Users/AlejandroMurillo/Desktop/Laboratorio6/medellin_graph.txt", "w", encoding="utf-8-sig") as file:
#     text_file = file.write(medellin_graph.draw_graph())