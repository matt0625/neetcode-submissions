class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []

            graph[a].append(b)


        visited = set()
        for k in graph.keys():
            path = set()
            if self.detectCycle(graph, k, path, visited):
                return False

            
        return True


    def detectCycle(self, graph, key, path, visited):
        if key in path:
            return True

        if key in visited:
            return False

        path.add(key)

        for neighbour in graph.get(key, []):
            if self.detectCycle(graph, neighbour, path, visited):
                return True

        path.remove(key)
        visited.add(key)

        return False


        

        
