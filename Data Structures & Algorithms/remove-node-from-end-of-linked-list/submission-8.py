# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        current = head 

        while current:
            length += 1
            current = current.next

        needed_node = length - n


        current = head
        prev = None
        while current:
            if needed_node == 0:
                if current is head:
                    head = head.next

                if prev:
                    prev.next = current.next

                return head

            needed_node -= 1
            prev = current
            current = current.next
 