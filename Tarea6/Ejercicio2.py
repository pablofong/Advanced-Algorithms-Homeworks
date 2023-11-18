#REFERENCE https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/
#geeks4geeks. (2012, March 20). Breadth First Search or BFS for a Graph. GeeksforGeeks; GeeksforGeeks. https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
#geeks4geeks. (2012, March 15). Depth First Search or DFS for a Graph. GeeksforGeeks; GeeksforGeeks. https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

import heapq
from collections import deque

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
    def uniform_cost_search(self, start_vertex, end_vertex):
        visited = set()
        heap = [(0, start_vertex, [start_vertex])]
        while heap:
            (cost, current_vertex, path) = heapq.heappop(heap)
            if current_vertex == end_vertex:
                return (cost, path)
            if current_vertex not in visited:
                visited.add(current_vertex)
                for neighbor_index, edge_cost in enumerate(self._adjacency_matrix[self._vertices.index(current_vertex)]):
                    if edge_cost > 0 and self._vertices[neighbor_index] not in visited:
                        heapq.heappush(heap, (cost + edge_cost, self._vertices[neighbor_index], path + [self._vertices[neighbor_index]]))
        return (float("inf"), None)
    
    def BFS(self, start_vertex, end_vertex):
        visited = set()
        queue = deque([(start_vertex, [start_vertex])])
        visited.add(start_vertex)
        while queue:
            current_vertex, path = queue.popleft()
            if current_vertex == end_vertex:
                return path
            for neighbor_index, edge_cost in enumerate(self._adjacency_matrix[self._vertices.index(current_vertex)]):
                if edge_cost > 0 and self._vertices[neighbor_index] not in visited:
                    new_path = path + [self._vertices[neighbor_index]]
                    queue.append((self._vertices[neighbor_index], new_path))
                    visited.add(self._vertices[neighbor_index])

    def DFS(self, start_vertex, end_vertex, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(start_vertex)
        path.append(start_vertex)
        if start_vertex == end_vertex:
            return path
        for neighbor_index, edge_cost in enumerate(self._adjacency_matrix[self._vertices.index(start_vertex)]):
            if edge_cost > 0 and self._vertices[neighbor_index] not in visited:
                new_path = self.DFS(
                    self._vertices[neighbor_index], end_vertex, visited, path
                )
                if new_path:
                    return new_path
        path.pop()
# ------------------------------------------------------------------------------------------------------------------
print("----Undirected graph----")

gr = WeightedGraph(directed=False)

# Add vertices to the graph
gr.add_vertex(0) #Togend
gr.add_vertex(1) #Blebus
gr.add_vertex(2) #Ontdale
gr.add_vertex(3) #Goding
gr.add_vertex(4) #Oriaron
gr.add_vertex(5) #Ylane
gr.add_vertex(6) #Strento
gr.add_vertex(7) #Zrusall
gr.add_vertex(8) #Duron
gr.add_vertex(9) #Ertonwell
gr.add_vertex(10)#Lagos
gr.add_vertex(11)#Niaphia
gr.add_vertex(12)#Adaset
gr.add_vertex(13)#Goxmont

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
# Uniform Cost
cost, path_uniform_cost = gr.uniform_cost_search(start_vertex, end_vertex)
print(f"Togend and Zrussal:")
print(f"Uniform cost path:")
print(path_uniform_cost)
#  BFS
print("BFS:")
path_bfs = gr.BFS(start_vertex, end_vertex)
print(path_bfs)
#  DFS
print("DFS:")
path_dfs = gr.DFS(start_vertex, end_vertex)
print(path_dfs)
# Clear graph
gr.clear()
