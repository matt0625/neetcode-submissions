import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for xi, yi in points:
            heapq.heappush_max(heap, (self.distance(xi, yi), xi, yi))
            if len(heap) > k:
                heapq.heappop_max(heap)

        res = []
        for d, x, y in heap:
            res.append([x, y])
        
        return res

    def distance(self, x, y):
        return x*x + y*y
        