#REFERENCE https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/
import heapq
class WeightedGraph:
    def __init__(self, directed: bool = False):
        self._directed = directed
        self._vertices = []
        self._adjacency_matrix = []

    def clear(self):
        self._vertices = []
        self._adjacency_matrix = []

    def number_of_vertices(self):
        return len(self._vertices)

    def vertices(self):
        return self._vertices

    def edges(self):
        e = []

        n = len(self._vertices)

        if self._directed:
            for i in range(n):
                for j in range(n):
                    if (self._adjacency_matrix[i][j] > 0):
                        e.append(
                            (self._vertices[i], self._vertices[j], self._adjacency_matrix[i][j]))
        else:
            for i in range(n):
                for j in range(i+1, n):
                    if (self._adjacency_matrix[i][j] > 0):
                        e.append(
                            (self._vertices[i], self._vertices[j], self._adjacency_matrix[i][j]))
        return e

    def add_vertex(self, v):
        if v in self._vertices:
            print("Warning: Vertex ", v, " already exists")
        else:
            self._vertices.append(v)
            n = len(self._vertices)
            if n > 1:
                for vertex in self._adjacency_matrix:
                    vertex.append(0)
            self._adjacency_matrix.append(n*[0])

    def remove_vertex(self, v):
        if v not in self._vertices:
            print("Warning: Vertex ", v, " does not exist")

        else:
            index = self._vertices.index(v)

            self._vertices.pop(index)

            for row in self._adjacency_matrix:
                row.pop(index)

            self._adjacency_matrix.pop(index)

    def add_edge(self, v1, v2, e=0):
        if v1 not in self._vertices:
            print("Warning: Vertex ", v1, " does not exist.")

        elif v2 not in self._vertices:
            print("Warning: Vertex ", v2, " does not exist.")

        elif not self._directed and v1 == v2:
            print("Warning: An undirected graph cannot have autocycles.")

        else:
            index1 = self._vertices.index(v1)
            index2 = self._vertices.index(v2)
            self._adjacency_matrix[index1][index2] = e

            if not self._directed:
                self._adjacency_matrix[index2][index1] = e

    def remove_edge(self, v1, v2):
        if v1 not in self._vertices:
            print("Warning: Vertex ", v1, " does not exist.")

        elif v2 not in self._vertices:
            print("Warning: Vertex ", v2, " does not exist.")

        else:
            index1 = self._vertices.index(v1)
            index2 = self._vertices.index(v2)
            self._adjacency_matrix[index1][index2] = 0

            if not self._directed:
                self._adjacency_matrix[index2][index1] = 0

    def adjacent_vertices(self, v):
        """ 
            Adjacent vertices of a vertex.

            param v: The vertex whose adjacent vertices are to be returned.
            return: The list of adjacent vertices of v.
        """

        if v not in self._vertices:
            # The vertex is not in the graph.
            print("Warning: Vertex ", v, " does not exist.")
            return []

        else:
            adjacent_list = []

            n = len(self._vertices)
            i = self._vertices.index(v)

            for j in range(n):
                if self._adjacency_matrix[i][j] != 0:
                    adjacent_list.append(
                        (self._vertices[j], self._adjacency_matrix[i][j]))

            return adjacent_list

    def is_adjacent(self, v1, v2) -> bool:
        if v1 not in self._vertices:
            print("Warning: Vertex ", v1, " does not exist.")
            return False

        elif v2 not in self._vertices:
            print("Warning: Vertex ", v2, " does not exist.")
            return False

        else:

            i = self._vertices.index(v1)
            j = self._vertices.index(v2)

            return self._adjacency_matrix[i][j] != 0

    def print_graph(self):
        # This method shows the edges of the graph.
        n = len(self._vertices)
        for i in range(n):
            for j in range(n):
                if self._adjacency_matrix[i][j] != 0:
                    print(self._vertices[i], " -> ", self._vertices[j],
                          " edge weight: ", self._adjacency_matrix[i][j])

    # UNIFORM COST
    def uniform_cost_search(self, start_vertex):
        visited = set()
        heap = [(0, start_vertex, [start_vertex])]
        while heap:
            (cost, current_vertex, path) = heapq.heappop(heap)
            if current_vertex not in visited:
                visited.add(current_vertex)
                if len(visited) == len(self._vertices):
                    return (cost, path)
                for neighbor_index, edge_cost in enumerate(self._adjacency_matrix[self._vertices.index(current_vertex)]):
                    if edge_cost > 0 and self._vertices[neighbor_index] not in visited:
                        heapq.heappush(heap, (cost + edge_cost, self._vertices[neighbor_index], path + [self._vertices[neighbor_index]]))
        return (float("inf"), None)
# ------------------------------------------------------------------------------------------------------------------
print("----Undirected graph----")

gr = WeightedGraph(directed=False)

# Add vertices to the graph
gr.add_vertex(1)
gr.add_vertex(2)
gr.add_vertex(3)
gr.add_vertex(4)
gr.add_vertex(5)
gr.add_vertex(6)
gr.add_vertex(7)
gr.add_vertex(8)
gr.add_vertex(9)
gr.add_vertex(10)
gr.add_vertex(11)
gr.add_vertex(12)
gr.add_vertex(13)
gr.add_vertex(14)
gr.add_vertex(15)
gr.add_vertex(16)
gr.add_vertex(17)
gr.add_vertex(18)
gr.add_vertex(19)
gr.add_vertex(20)

# Add edges to the graph
gr.add_edge(1, 2, 1)
gr.add_edge(1, 3, 1)
gr.add_edge(2, 3, 3)
gr.add_edge(3, 4, 4)
gr.add_edge(4, 1, 5)
gr.add_edge(4, 3, 7)
gr.add_edge(4, 5, 5)
gr.add_edge(5, 2, 2)
gr.add_edge(6, 1, 2)
gr.add_edge(6, 5, 3)
gr.add_edge(7, 2, 4)
gr.add_edge(7, 6, 2)
gr.add_edge(8, 3, 5)
gr.add_edge(8, 7, 1)
gr.add_edge(9, 4, 2)
gr.add_edge(9, 8, 4)
gr.add_edge(10, 5, 3)
gr.add_edge(10, 9, 3)
gr.add_edge(11, 6, 2)
gr.add_edge(11, 10, 2)
gr.add_edge(12, 7, 4)
gr.add_edge(12, 11, 1)
gr.add_edge(13, 8, 3)
gr.add_edge(13, 12, 5)
gr.add_edge(14, 9, 1)
gr.add_edge(14, 13, 2)
gr.add_edge(15, 10, 4)
gr.add_edge(15, 14, 3)
gr.add_edge(16, 11, 2)
gr.add_edge(16, 15, 2)
gr.add_edge(17, 12, 3)
gr.add_edge(17, 16, 4)
gr.add_edge(18, 13, 2)
gr.add_edge(18, 17, 1)
gr.add_edge(19, 14, 3)
gr.add_edge(19, 18, 2)
gr.add_edge(20, 15, 4)
gr.add_edge(20, 19, 3)

# Show graph

gr.print_graph()
# Realiza la búsqueda de costo uniforme desde el primer nodo del grafo
cost, path = gr.uniform_cost_search(gr.vertices()[0])

print("Costo mínimo:", cost)
print("Camino óptimo:", path)
# Clear graph
gr.clear()
