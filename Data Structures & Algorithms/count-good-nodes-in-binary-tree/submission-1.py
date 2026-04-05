# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:



        def dfs(node,premax):
            res=0
            if not node:
                return res

            if node.val>=premax:
                premax=node.val
                res+=1

            res+=dfs(node.left,premax)
            res+=dfs(node.right,premax)

            return res

        

        return dfs(root,float("-inf"))
            
        