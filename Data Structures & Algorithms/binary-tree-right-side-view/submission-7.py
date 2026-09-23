# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # strategy: similar BFS technique to before but this time only add last value in unvisited at each step
        if not root: return []

        res = []
        unvisited = deque([root])
        while unvisited:
            n = len(unvisited)
            while n:
                current = unvisited.popleft()
                if current.left:
                    unvisited.append(current.left)
                if current.right:
                    unvisited.append(current.right)
                n -= 1
            
            res.append(current.val)
        
        return res
        
