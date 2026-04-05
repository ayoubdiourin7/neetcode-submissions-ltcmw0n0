# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        def dfs(pre, ino):
            if not pre:
                return None
            rootval=pre[0]
            rootindex=ino.index(rootval)

            leftino=ino[:rootindex]
            rightino=ino[rootindex+1:]

            leftpre=pre[1:rootindex+1]
            rightpre=pre[rootindex+1:]

            return TreeNode(rootval,dfs(leftpre,leftino),dfs(rightpre,rightino))

        return dfs(preorder,inorder)




        