class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[]
        stack =[]
        ans = [0]*len(temp)
        for curi in range(0,len(temp)):
            while stack and temp[curi]>temp[stack[-1]]:  
                previ=stack.pop()
                ans[previ]=(curi -previ)

            
            stack.append(curi)
        return ans



        