# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        l=[root]
        depths=[0]
        res=0
        while len(l)>0 :

            nood=l.pop()
            d=depths.pop()

            if nood:
                l.append(nood.left)
                l.append(nood.right)
                depths.append(d+1)
                depths.append(d+1)

            res= max(d,res)
        return res
            
            
            


