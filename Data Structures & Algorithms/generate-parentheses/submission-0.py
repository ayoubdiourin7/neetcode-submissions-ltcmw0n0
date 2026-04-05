class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        res=[]

        def dfs(nOpen,nOclose,currparenthese):
            if nOpen==0 and len(currparenthese)==2*n :
                res.append(currparenthese)
                return 
            if nOpen > 0:
                dfs(nOpen-1,nOclose,currparenthese+"(")
            if  0 <= nOpen < nOclose:
                dfs(nOpen,nOclose-1,currparenthese+")")
            return 

        dfs(n,n,"")
        return res




        