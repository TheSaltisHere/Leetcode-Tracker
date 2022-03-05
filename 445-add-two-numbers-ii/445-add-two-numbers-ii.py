# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=""
        b=""
        while l1:
            
            a=a+str(l1.val)
            l1=l1.next
            
        while l2:
            
            b=b+str(l2.val)
            l2=l2.next
            
        c=list(str(int(a)+int(b)))
        
        
        value =ListNode(int(c.pop(0)))
        head=value
        
        while c:
            value.next=ListNode(int(c.pop(0)))
            value = value.next
		
        return head
        
        
            
        