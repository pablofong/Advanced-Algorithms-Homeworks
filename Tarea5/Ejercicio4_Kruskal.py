class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal_mst(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        ds = DisjointSet(self.V)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = ds.find(u)
            y = ds.find(v)
            if x != y:
                e += 1
                result.append([u, v, w])
                ds.union(x, y)

        return result


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

result = g.kruskal_mst()

for u, v, w in result:
    print(f"Edge: {u} - {v}, Weight: {w}")
