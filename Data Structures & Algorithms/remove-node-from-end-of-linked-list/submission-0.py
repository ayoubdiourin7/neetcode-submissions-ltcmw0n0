# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fastPointer=head
        slowPointer=head

        i=0
        while fastPointer and i<=n :
            i+=1
            fastPointer=fastPointer.next
        if i==n:
            return head.next
        while fastPointer:
            fastPointer=fastPointer.next
            slowPointer=slowPointer.next
        
        slowPointer.next=slowPointer.next.next
        return head 
            
        


        