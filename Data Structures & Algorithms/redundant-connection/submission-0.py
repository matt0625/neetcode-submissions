class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]

        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[x_root] = y_root
            return True

        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ccs = UnionFind(n)

        r1, r2 = 0, 0
        for a, b in edges:
            if not ccs.union(a, b):
                r1, r2 = a, b
        
        return [r1, r2]
