# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(root: Optional[TreeNode], subRooot: Optional[TreeNode]):
            if  root is None and  subRooot is None:
                return True
            elif root and subRooot and root.val == subRooot.val :

                return (compare(root.left,subRooot.left) and compare(root.right,subRooot.right))

            else:
                return False
        if compare(root , subRoot):
            return True
        elif root is None:
            return False
        else :
            return self.isSubtree(root.right , subRoot)  or self.isSubtree(root.left , subRoot)

        

                
        