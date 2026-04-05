# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def findAncestors(currNode ,target,res):
            
            res.append(currNode)

            if currNode.val == target:
                return res
            if target<currNode.val:
                return findAncestors(currNode.left ,target,res)
            else:
                return  findAncestors(currNode.right ,target,res)
        
        lp = findAncestors(root,p.val,[])
        lq = findAncestors(root,q.val,[])
        
        minlen = min(len(lq),len(lp))
        res=root.val
        for i in range(minlen):
            if lp[i].val == lq[i].val :
                res=lp[i]

        return res



            
