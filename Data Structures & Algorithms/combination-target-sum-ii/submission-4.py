class Solution:
    def combinationSum2(self, c: List[int], target: int) -> List[List[int]]:

        res=set()
        c.sort()
        def  backtrack(i,currSum,currlist):

            if currSum == target:
                res.add(tuple(currlist[::]))
                return 
            if len(c)<=i or currSum>target:
                return 
            elif currSum < target:
                currlist.append(c[i])
                backtrack(i+1,currSum+c[i],currlist)
                currlist.pop()
                backtrack(i+1,currSum,currlist[::])
                
        backtrack(0,0,[])
            
        return [list(l) for l in res]
            





                 

            
    


        



        


        