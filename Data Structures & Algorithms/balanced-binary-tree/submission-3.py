# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        if abs(self.maxHeight(root.left) - self.maxHeight(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxHeight(self, root):
        if not root: return 0

        return max(self.maxHeight(root.left), self.maxHeight(root.right)) + 1