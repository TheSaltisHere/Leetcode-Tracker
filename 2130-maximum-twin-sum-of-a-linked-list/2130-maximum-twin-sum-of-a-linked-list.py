# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        l=[]
        summation=[]
        while head:
            l.append(head.val)
            head=head.next
            
        for i in range(int(len(l)/2)):
            summation.append(l[i]+l[-1-i])
        return  max(summation)
            
            
            
        