"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        nodemap = {}

        current = head
        while current:
            nodemap[current] = Node(current.val)
            current = current.next

        # 2 passes = O(n)
        current = head
        while current:
            nodemap[current].next = nodemap.get(current.next)
            nodemap[current].random = nodemap.get(current.random)
            current = current.next

        return nodemap[head]
        


