# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res=True
        def depth(nood):
            
            if nood is None:
                return 0
            l=depth(nood.left)
            r=depth(nood.right)
            if not abs(l-r)<=1:
                self.res=False
            return 1+max(l,r)

        depth(root)
        return self.res