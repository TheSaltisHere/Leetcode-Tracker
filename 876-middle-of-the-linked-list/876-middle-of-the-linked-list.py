# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        count1=0
        head1=head
        while head:
            count=count+1
            head=head.next
        
        a=int(count/2)+1
        print(a)
            
        while head1:
            count1=count1+1
            
            if count1==a:
                return head1
            else:
                head1=head1.next
            
        