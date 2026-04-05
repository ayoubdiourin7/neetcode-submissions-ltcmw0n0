# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        res=[]
        temp=[]
        q=deque([root])
    
        while q:
            lenq=len(q)
            for i in range(lenq):
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(temp)
            temp=[]

        return res

            


        