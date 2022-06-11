# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Allocates a new node with given data
def newNode(data):
    new_node = ListNode(data)
    new_node.data = data
    new_node.next = None
    return new_node
 
# Function to insert a new node at the
# end of linked list using recursion.
def insertEnd(head, data):
    if (head == None):
        return newNode(data)
 
    # If we have not reached end,
    # keep traversing recursively.
    else:
        head.next = insertEnd(head.next, data)
        return head
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=[]
        length=0
        head_dup=head
        while head_dup:
            head_dup=head_dup.next
            length=length+1
            
        for i in range(length):
            l.append(head.val)
            head=head.next
            
        l.pop(length-n)
        
        head_main=None
        for i in l:
            head_main=insertEnd(head_main,i)
        
        return head_main