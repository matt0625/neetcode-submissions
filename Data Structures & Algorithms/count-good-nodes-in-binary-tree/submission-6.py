# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # strategy: dfs along all paths from root, store max value on path and compare it to the value of each node as we process it, if it is good then increment the count and update maxvalue
        return self.dfs(root)



    
    def dfs(self, node, maxvalue=float('-inf')):
        if not node:
            return 0

        if node.val >= maxvalue:
            maxvalue = node.val         

            return self.dfs(node.left, maxvalue) +  self.dfs(node.right,     maxvalue) + 1
        
        return self.dfs(node.left, maxvalue) +  self.dfs(node.right, maxvalue)
       
        