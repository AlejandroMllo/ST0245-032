import GraphAL


class Graph(GraphAL.GraphAL):
    """
    Implementation of a simple graph, where:
        - No node has an edge to itself.
        - The graph is not directed. If a is
          connected with b, then b is connected
          with a.
        - The graph is strongly connected.
        - Vertices' successors are stored in an adjacency list.
    """

    def insert_edge(self, vertex, successor, weight = 0):
        if vertex not in self.vertices:
            self.insert_vertex(vertex)
        if successor not in self.vertices:
            self.insert_vertex(successor)

        super(Graph, self).insert_edge(vertex, successor, weight)
        super(Graph, self).insert_edge(successor, vertex, weight)
        
    def is_bipartite(self, start_vertex):
        """
        Checks whether the graph is bipartite.
        It means that it is acyclic or that all
        its cycles are of even length.
        :return: Boolean.
        """

        def __expand_vertex(v, parent = None):
            """
            :param v: The vertex to be expanded.
            :return: List of successor vertices.
            """
            successors = []
            current_vertex = self.get_successors(v).head
            while current_vertex is not None:
                data = current_vertex.data[0]
                if v != data and data != parent:
                    successors.append(data)
                current_vertex = current_vertex.next

            return successors

        color1 = set()
        color2 = set()

        fringe = [start_vertex]
        visited_vertices = set()
        expansion = set()
        iteration = 0
        while len(visited_vertices) < len(self.vertices):

            for element in fringe:

                if element in visited_vertices:
                    continue

                visited_vertices.add(element)
                expansion = set(__expand_vertex(element)) - visited_vertices

                if iteration % 2 == 0:

                    if color2.intersection({element}) != set():
                        return False
                    else:
                        color1.add(element)

                    if color1.intersection(expansion) != set():
                        return False
                    else:
                        color2 = color2.union(expansion)
                else:

                    if color1.intersection({element}) != set():
                        return False
                    else:
                        color2.add(element)

                    if color2.intersection(expansion) != set():
                        return False
                    else:
                        color1 = color1.union(expansion)

            fringe += list(expansion)
            iteration += 1

        return True


def bipartite_graph():

    graphs = []

    def prompt():
        num_nodes = eval(input())
        if num_nodes == 0:
            return 0, None
        num_edges = eval(input())
        return num_nodes, num_edges

    nodes, edges = prompt()
    connection = nodes
    while nodes != 0:

        graph = Graph()

        for _ in range(edges):
            connection = input().split()
            graph.insert_edge(connection[0], connection[1])

        graphs.append(graph.is_bipartite(connection[0]))
        nodes, edges = prompt()

    for g in graphs:
        if g:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")

bipartite_graph()
