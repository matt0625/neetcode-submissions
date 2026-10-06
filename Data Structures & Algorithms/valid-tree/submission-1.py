class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree if connected and has n-1 edges
        # so dfs from any node and see if you can reach all others
        # also check len(edges) == n-1
        if len(edges) != n - 1: return False
        if not edges and n == 1: return True
        
        graph = {}
        for a, b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append(b)
            graph[b].append(a)
    
        seen = set()
        k, _ = edges[0]
        self.dfs(graph, seen, k)

        return len(seen) == n
    


    def dfs(self, graph, seen, start):
        seen.add(start)
        for neighbour in graph.get(start, []):
            if neighbour in seen:
                continue

            self.dfs(graph, seen, neighbour)

                

