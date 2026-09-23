# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True

        return self.dfs(root)
        



    def dfs(self, node, lb=float('-inf'), ub=float('inf')):
        if not node:
            return True

        if lb < node.val < ub:
            return self.dfs(node.left, lb, node.val) and self.dfs(node.right, node.val, ub)
        else:
            return False

        

        

            