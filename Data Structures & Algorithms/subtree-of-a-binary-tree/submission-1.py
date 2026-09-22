# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False

        unvisited = deque([root])
        while unvisited:
            current = unvisited.popleft()

            if current.val == subRoot.val:
                if self.isSameTree(current, subRoot):
                    return True
        
            if current.left:
                unvisited.append(current.left)

            if current.right:
                unvisited.append(current.right)
            
        return False
        


    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        elif not p or not q:
            return False

        elif p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)