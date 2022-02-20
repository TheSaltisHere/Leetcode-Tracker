# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head, previous=None):
        if not head:
            return previous
        next = head.next
        head.next = previous
        return self.reverseList(next, head)