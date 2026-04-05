# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(currNode,minh,maxh):
            if not currNode:
                return True

            leftb= (minh < currNode.left.val and currNode.left.val < currNode.val  ) if currNode.left else True
            rightb= currNode.right.val<maxh   and  currNode.val < currNode.right.val if currNode.right else True
            

            if  leftb and rightb:
                return dfs(currNode.left ,minh ,min(maxh ,currNode.val )) and dfs(currNode.right ,max(minh ,currNode.val ) , maxh)
            
            return False
        return dfs(root,float("-inf") ,float("inf"))

        