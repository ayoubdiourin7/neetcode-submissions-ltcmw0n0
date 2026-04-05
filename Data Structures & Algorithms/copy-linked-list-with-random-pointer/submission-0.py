"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        headCopy=Node(-1)
        currCopy=headCopy
        currnode=head

        save={}

        while currnode != None:
            
            if currnode in save:
                copy=save[currnode]
            else:
                copy=Node(currnode.val,None,None)
                save[currnode]=copy
            random=None
            if currnode.random in save :
                random=save[currnode.random]
            elif currnode.random:
                random=Node(currnode.random.val,None,None)
                save[currnode.random]=random

            copy.random=random
            currCopy.next=copy
            currnode=currnode.next
            currCopy=currCopy.next
        return headCopy.next


        