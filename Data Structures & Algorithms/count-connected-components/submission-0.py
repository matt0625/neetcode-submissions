class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]

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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        ccs = UnionFind(n)
        for a, b in edges:
            if ccs.union(a, b):
                res -= 1

        return res