#Reference https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def prim_mst(self):
        max_val = float('inf')
        key = [max_val] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return parent

    def min_key(self, key, mst_set):
        min_val = float('inf')
        min_index = None
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        return min_index



g = Graph(14)

g.add_edge(0, 1, 121)
g.add_edge(0, 2, 210)
g.add_edge(2, 3, 98)
g.add_edge(2, 1, 165)
g.add_edge(2, 4, 219)
g.add_edge(3, 5, 88)
g.add_edge(5, 6, 99)
g.add_edge(5, 4, 117)
g.add_edge(6, 7, 121)
g.add_edge(6, 4, 221)
g.add_edge(4, 1, 291)
g.add_edge(1, 8, 160)
g.add_edge(8, 9, 121)
g.add_edge(8, 10, 119)
g.add_edge(9, 11, 300)
g.add_edge(10, 11, 56)
g.add_edge(10, 12, 130)
g.add_edge(13, 7, 112)
g.add_edge(13, 11, 212)
g.add_edge(13, 12, 103)
g.add_edge(7, 12, 15)

parents = g.prim_mst()
for i in range(1, g.V):
    print(f"Edge: {parents[i]} - {i}, Weight: {g.graph[i][parents[i]]}")
