# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        curl1=l1
        curl2=l2
        carry=0
        head=ListNode()
        curr=head

        while curl1 or curl2 or carry:
            val1= curl1.val if curl1 else 0
            curl1=curl1.next if curl1 else None
            val2= curl2.val if curl2 else 0
            curl2=curl2.next if curl2 else None
            valnode=(val1+val2+carry)%10
            carry=(val1+val2+carry)//10
            curr.next=ListNode(valnode)
            curr=curr.next



        return head.next




        