# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []

        unvisited = deque([root])
        while unvisited:
            n = len(unvisited)
            tmp = []
            while n != 0:
                node = unvisited.popleft()
                tmp.append(node.val)
                if node.left:
                    unvisited.append(node.left)
                if node.right:
                    unvisited.append(node.right)

                n -= 1

            res.append(tmp)

        return res