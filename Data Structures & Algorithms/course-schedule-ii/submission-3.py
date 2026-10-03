class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []

            graph[a].append(b)


        visited = set()
        res = []
        for k in graph.keys():
            path = set()
            if self.detectCycle(graph, k, path, visited, res):
                return []


        for i in range(numCourses):
            if i not in res:
                res.append(i)

        return res


    def detectCycle(self, graph, key, path, visited, res):
        if key in path:
            return True

        if key in visited:
            return False

        path.add(key)

        for neighbour in graph.get(key, []):
            if self.detectCycle(graph, neighbour, path, visited, res):
                return True

        res.append(key)
        path.remove(key)
        visited.add(key)

        return False