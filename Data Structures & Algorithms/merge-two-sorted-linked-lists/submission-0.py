# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currehead1=head1
        currehead2=head2

        head=ListNode(0,None)
        curr=head
        while currehead2 or currehead1:
            val1 = currehead1.val if currehead1 else float("inf")
            val2 = currehead2.val if currehead2 else float("inf")
            if val1<val2:
                curr.next=currehead1
                currehead1=currehead1.next
            else:
                curr.next=currehead2
                currehead2=currehead2.next
            curr=curr.next
        
        return head.next
        





        