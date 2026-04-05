# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        res=0

        def dfs(node,premax):
            nonlocal res
            if not node:
                return 

            if node.val>=premax:
                premax=node.val
                res+=1

            dfs(node.left,premax)
            dfs(node.right,premax)

            return 

        dfs(root,float("-inf"))

        return res
            
        