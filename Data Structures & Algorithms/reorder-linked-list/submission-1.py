# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fastPointer=slowPointer=head

        while fastPointer and fastPointer.next  :
            slowPointer=slowPointer.next
            fastPointer=fastPointer.next.next

        # reverse the secon linkedList


        

        currSecond=slowPointer.next
        nextNode=None
        slowPointer.next=None
        while currSecond:
            temp = currSecond.next
            currSecond.next=nextNode
            nextNode=currSecond
            currSecond=temp
        
        #merge the 2
        curr= head
        currSecond =nextNode
        while currSecond:
            temp=curr.next
            curr.next=currSecond
            tempSecond = currSecond.next
            currSecond.next=temp
            curr=temp
            currSecond=tempSecond

        

            

        
        

        



        





        