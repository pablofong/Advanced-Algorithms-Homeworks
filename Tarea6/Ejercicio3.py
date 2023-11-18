# REFERENCE https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/
# https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
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

    def dijkstra(self, start_vertex, end_vertex):
        distances = {vertex: float('inf') for vertex in self._vertices}
        distances[start_vertex] = 0
        visited = set()
        heap = [(0, start_vertex)]

        while heap:
            current_distance, current_vertex = heapq.heappop(heap)
            visited.add(current_vertex)

            if current_vertex == end_vertex:
                shortest_path = [end_vertex]
                while end_vertex != start_vertex:
                    for neighbor_index, edge_cost in enumerate(self._adjacency_matrix[self._vertices.index(end_vertex)]):
                        if edge_cost > 0 and distances[end_vertex] == distances[self._vertices[neighbor_index]] + edge_cost:
                            shortest_path.insert(
                                0, self._vertices[neighbor_index])
                            end_vertex = self._vertices[neighbor_index]
                            break
                return distances[current_vertex], shortest_path

            for neighbor_index, edge_cost in enumerate(self._adjacency_matrix[self._vertices.index(current_vertex)]):
                if edge_cost > 0 and self._vertices[neighbor_index] not in visited:
                    new_distance = current_distance + edge_cost
                    if new_distance < distances[self._vertices[neighbor_index]]:
                        distances[self._vertices[neighbor_index]
                                  ] = new_distance
                        heapq.heappush(
                            heap, (new_distance, self._vertices[neighbor_index]))

        return float("inf"), None

    def floyd_warshall_distance(self, start_vertex, end_vertex):
        n = len(self._vertices)
        dist = [row[:] for row in self._adjacency_matrix]
        start_index = self._vertices.index(start_vertex)
        end_index = self._vertices.index(end_vertex)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != 0 and dist[k][j] != 0:
                        if dist[i][j] == 0 or dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
        return dist[start_index][end_index]

    def print_graph(self):
        # This method shows the edges of the graph.
        n = len(self._vertices)
        for i in range(n):
            for j in range(n):
                if self._adjacency_matrix[i][j] != 0:
                    print(self._vertices[i], " -> ", self._vertices[j],
                          " edge weight: ", self._adjacency_matrix[i][j])


# ------------------------------------------------------------------------------------------------------------------
print("----Undirected graph----")

gr = WeightedGraph(directed=False)

# Add vertices to the graph
gr.add_vertex(0)  # Togend
gr.add_vertex(1)  # Blebus
gr.add_vertex(2)  # Ontdale
gr.add_vertex(3)  # Goding
gr.add_vertex(4)  # Oriaron
gr.add_vertex(5)  # Ylane
gr.add_vertex(6)  # Strento
gr.add_vertex(7)  # Zrusall
gr.add_vertex(8)  # Duron
gr.add_vertex(9)  # Ertonwell
gr.add_vertex(10)  # Lagos
gr.add_vertex(11)  # Niaphia
gr.add_vertex(12)  # Adaset
gr.add_vertex(13)  # Goxmont

# Add edges to the graph
gr.add_edge(0, 1, 121)
gr.add_edge(0, 2, 210)
gr.add_edge(2, 3, 98)
gr.add_edge(2, 1, 165)
gr.add_edge(2, 4, 219)
gr.add_edge(3, 5, 88)
gr.add_edge(5, 6, 99)
gr.add_edge(5, 4, 117)
gr.add_edge(6, 7, 121)
gr.add_edge(6, 4, 221)
gr.add_edge(4, 1, 291)
gr.add_edge(1, 8, 160)
gr.add_edge(8, 9, 121)
gr.add_edge(8, 10, 119)
gr.add_edge(10, 11, 300)
gr.add_edge(9, 11, 56)
gr.add_edge(9, 12, 130)
gr.add_edge(13, 7, 112)
gr.add_edge(13, 11, 212)
gr.add_edge(13, 12, 103)
gr.add_edge(7, 12, 15)

# Show graph

# gr.print_graph()

start_vertex = 0
end_vertex = 7
shortest_distance_dijsta, shortest_path_djista = gr.dijkstra(start_vertex, end_vertex)
print("Dijstra Algorithm")
print(f"Shortest distance fromTogend and Zrusall: {shortest_distance_dijsta}")
shortest_distance_floyd = gr.floyd_warshall_distance(start_vertex, end_vertex)
print("\nFloyd Warshall Algorithm")
print(f"Shortest distance from Togend and Zrusall: {shortest_distance_floyd}")
# Clear graph
gr.clear()
