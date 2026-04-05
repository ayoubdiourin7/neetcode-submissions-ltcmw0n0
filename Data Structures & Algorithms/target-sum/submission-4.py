class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        save={}
        res=0
        def dfs(i,subsum):
            if (i,subsum) in save:
                return save[(i,subsum)]

            if i == len(nums):
                return  1 if subsum == target else 0
            else:
                save[(i,subsum)] = dfs(i+1,subsum+nums[i]) + dfs(i+1,subsum-nums[i])
            return save[(i,subsum)]

        return dfs(0,0)

    

        