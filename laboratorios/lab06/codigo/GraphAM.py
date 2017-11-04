

class GraphAM:
    """
    Basic implementation of a graph
    whose edges are stored in an
    adjacency matrix.
    """

    def __init__(self):
        self.vertices = [[None]]

    def insert_vertex(self, vertex):
        """
        Inserts a vertex to the graph.
        Raises an AttributeError if the
        vertex is already in the graph.
        :param vertex: The vertex to be inserted.
        :return: Void.
        """
        if vertex not in self.vertices:
            self.vertices[0].append(vertex)
            self.vertices.append([vertex])
            for v in range(1, len(self.vertices[0])):
                self.vertices[v] += [None] * (len(self.vertices[0]) - len(self.vertices[v]))
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
        if vertex in self.vertices[0]:
            if successor not in self.vertices[0]:
                self.insert_vertex(successor)
            vertex_index = self.vertices[0].index(vertex)
            successor_index = self.vertices[0].index(successor)
            self.vertices[vertex_index][successor_index] = weight
        else:
            raise AttributeError("This vertex is not in the graph.")

    def get_successors(self, vertex):
        """
        Returns the successor of vertex.
        If vertex does not exist, it raises
        an AttributeError.
        :param vertex: The vertex whose successors are to be retrieved.
        :return: Void
        """
        if vertex in self.vertices[0]:
            vertex_index = self.vertices[0].index(vertex)
            successors = self.vertices[vertex_index]
            real_successors = []
            for index, successor in enumerate(successors):
                if successor is not None and index != 0:
                    real_successors.append((self.vertices[index][0], successor))

            return real_successors
        else:
            raise AttributeError("This vertex is not in the graph.")

    def get_vertex_with_more_successors(self):
        """
        Returns the vertex with more
        successors.
        :return: Array representation of vertex.
        """

        if len(self.vertices) < 1:
            raise AttributeError("Not enough vertices in the graph.")

        vertex_with_more_successors = self.vertices[1]
        for vertex in self.vertices[1:]:
            if len(vertex) - vertex.count(None) > len(vertex_with_more_successors) - vertex_with_more_successors.count(None):
                vertex_with_more_successors = vertex

        return vertex_with_more_successors

    def draw_graph(self):
        """
        Returns the code to draw the graph at
        http://webgraphviz.com/
        :return: String
        """

        graph = "digraph G {"
        for index in range(1, len(self.vertices[0])):
            vertex = self.vertices[0][index]
            successors = self.get_successors(vertex)
            for successor, weight in successors:
                graph += '\n\"' + str(vertex) + '\"' + " -> " + '\"' + str(successor) + '\"'
                graph += ((" [label = \"" + str(weight) + "\"] ") if weight != 0 else "")

        return graph + "\n}"

    def __str__(self):
        vertices_str = ""
        for vertex in self.vertices:
            vertices_str += str(vertex) + "\n"

        return vertices_str

graph = GraphAM()
graph.insert_vertices(2, 3, 5, 7, 8, 9, 10, 11)
graph.insert_edge(3, 8)
graph.insert_edge(3, 10)
graph.insert_edge(5, 11)
graph.insert_edge(7, 8)
graph.insert_edge(7, 11)
graph.insert_edge(8, 9)
graph.insert_edge(11, 2)
graph.insert_edge(11, 9)
graph.insert_edge(11, 11)

print("--- Adjacency Matrix Graph ---")
print(graph)
print("Successors 8: " + str(graph.get_successors(8)) + "\n")
print(graph.draw_graph())

more_successors = graph.get_vertex_with_more_successors()
print("\nVertex with more successors:", more_successors[0], "\n\tSuccessors:", more_successors[1:])