# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # standard BFS traversal, queue at each step is a snapshot of the level
        # if level counter is odd then we proceed with reversal
        level = 0
        queue = deque([root])

        while queue:
            n = len(queue)
            nodes = []

            for i in range(n):
                current = queue.popleft()
                nodes.append(current)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            if level % 2 == 1:
                left, right = 0, len(nodes) - 1
                while left <= right:
                    nodes[left].val, nodes[right].val = nodes[right].val, nodes[left].val
                    left += 1
                    right -= 1
                

            level += 1

        return root

            


            


