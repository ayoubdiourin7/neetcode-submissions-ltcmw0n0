class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        seen=set()
        def dfs(start , comb , total):
            sumComb = sum(comb)
            if sumComb == target:
                res.append(comb)
                return 
            elif sumComb < target :
                for i in range(start ,len(nums)) :
                    dfs(i, comb + [nums[i]],total+ nums[i])
        dfs(0,[],0)
        return res
             

