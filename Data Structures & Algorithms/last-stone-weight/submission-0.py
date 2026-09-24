import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            y = heapq.heappop_max(heap)
            x = heapq.heappop_max(heap)
            if x < y:
                heapq.heappush_max(heap, y-x)

        if heap:
            return heap[0]

        return 0