class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone={ "2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        stack=[]
        res=[]

        def dfs(i):
            if i == len(digits):
                res.append("".join(stack))
                return
            
            for c in phone[digits[i]]:
                stack.append(c)
                dfs(i+1)
                stack.pop()
            return 
        if len(digits) ==0 :
            return []
    
        dfs(0)
        return res



        