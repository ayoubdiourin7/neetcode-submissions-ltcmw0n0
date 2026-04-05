# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        right=head
        left=head

        while right and right.next:

            right=right.next.next
            left=left.next
            if left==right:
                return True


        return False



        