#REFERENCE https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_vertex(self, v):
        pass

    def add_edge(self, v1, v2, e=0):
        self.graph[v1 - 1][v2 - 1] = e

    def bfs(self, s, t, parent):
        visited = [False] * self.V
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if (not visited[ind]) and (val > 0):
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return visited[t]

    def ford_fulkerson(self, start_vertex, end_vertex):
        parent = [-1] * self.V
        max_flow = 0

        while self.bfs(start_vertex, end_vertex, parent):
            path_flow = float("Inf")
            s = end_vertex
            while s != start_vertex:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = end_vertex
            while v != start_vertex:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


g = Graph(14)
g.add_edge(0, 1, 70)
g.add_edge(0, 5, 37)
g.add_edge(0, 2, 80)
g.add_edge(1, 7, 72)
g.add_edge(2, 3, 54)
g.add_edge(3, 11, 82)
g.add_edge(4, 2, 44)
g.add_edge(4, 3, 69)
g.add_edge(4, 11, 71)
g.add_edge(5, 0, 43)
g.add_edge(5, 4, 47)
g.add_edge(5, 6, 24)
g.add_edge(6, 5, 25)
g.add_edge(6, 10, 76)
g.add_edge(7, 1, 85)
g.add_edge(7, 6, 61)
g.add_edge(7, 8, 23)
g.add_edge(8, 6, 82)
g.add_edge(8, 9, 60)
g.add_edge(9, 6, 42)
g.add_edge(9, 13, 90)
g.add_edge(10, 4, 66)
g.add_edge(10, 11, 50)
g.add_edge(10, 12, 42)
g.add_edge(10, 13, 34)
g.add_edge(11, 12, 66)
g.add_edge(12, 13, 75)
g.add_edge(13, 10, 55)

start_vertex = 0
end_vertex = 13
result = g.ford_fulkerson(start_vertex, end_vertex)
print(f"The maximum possible flow from A to N is {result}")
start_vertex = 1
end_vertex = 10
result = g.ford_fulkerson(start_vertex, end_vertex)
print(f"The maximum possible flow from B to K is {result}")
start_vertex = 2
end_vertex = 5
result = g.ford_fulkerson(start_vertex, end_vertex)
print(f"The maximum possible flow from C to F is {result}")