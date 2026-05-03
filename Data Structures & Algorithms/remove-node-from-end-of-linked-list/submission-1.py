# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        n_delay, p = dummy, head
        for _ in range(n):
            p = p.next 
        while p:
            p = p.next
            n_delay = n_delay.next
        
        n_delay.next = n_delay.next.next

        return dummy.next