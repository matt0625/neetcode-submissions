# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return

        while len(lists) > 1:
            mergedArr = []
            i = 1
            while i < len(lists):
                mergedHead = self.merge(lists[i-1], lists[i])
                mergedArr.append(mergedHead)
                i += 2
            
            if len(lists) % 2 == 1:
                mergedArr.append(lists[i-1])

            lists = mergedArr
                
        return lists[0]

    
    # take 2 heads of lists l1 and l2 and merge the nodes of l2 into l1
    def merge(self, head1, head2):
        dummy = ListNode()
        curr = dummy

        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next

        if head1 is not None:
            curr.next = head1
        else:
            curr.next = head2

        return dummy.next