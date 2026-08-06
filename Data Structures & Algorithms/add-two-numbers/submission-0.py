# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        from collections import deque
        dq1, dq2 = deque(), deque()
        
        cur = l1
        while cur:
            dq1.appendleft(cur.val)
            cur = cur.next  
        cur = l2
        while cur:
            dq2.appendleft(cur.val)
            cur = cur.next  
        val1 = 0  
        for num in dq1:
            val1 = val1 * 10 + num
            
        val2 = 0 
        for num in dq2:
            val2 = val2 * 10 + num
            
        total_str = str(val1 + val2)[::-1] 
        
        dummy = ListNode(0)
        cur = dummy
        for char in total_str:
            cur.next = ListNode(int(char))
            cur = cur.next    
        return dummy.next