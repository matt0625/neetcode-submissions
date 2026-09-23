# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # strategy: bfs to reach each node and maintain a max_heap of size k, then the top of the heap is the kth smallest value
        heap = []

        unvisited = deque([root])
        while unvisited:
            current = unvisited.popleft()
            heapq.heappush_max(heap, current.val)
            if len(heap) > k:
                heapq.heappop_max(heap)

            if current.left:
                unvisited.append(current.left)
            if current.right:
                unvisited.append(current.right)

        print(heap)
        return heapq.heappop_max(heap)

        