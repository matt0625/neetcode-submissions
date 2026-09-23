# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left and not root.right:
            return root.val

        maxsofar = float('-inf')

        def dfsPathSum(node): 
            nonlocal maxsofar
            if not node: return 0 
            
            left = dfsPathSum(node.left)
            right = dfsPathSum(node.right)

            this_subtree = node.val
            if left > 0:
                this_subtree += left
            if right > 0:
                this_subtree += right

            if this_subtree > maxsofar:
                maxsofar = this_subtree
            
            return max(0, left, right) + node.val
        
        dfsPathSum(root)
        return maxsofar
        

        

