class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res=[]
        stack =[]
        ans = [0]*len(temp)
        for curi in range(0,len(temp)):
            while stack:
                if temp[curi]>temp[stack[-1]]:
                    previ=stack.pop()
                    ans[previ]=(curi -previ)
                else :
                    break
            
            stack.append(curi)
        return ans



        