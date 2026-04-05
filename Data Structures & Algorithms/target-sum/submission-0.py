class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        res=0
        def dfs(i,subsum):
            if i == len(nums):
                return 1 if subsum == target else 0
            

            return dfs(i+1,subsum+nums[i]) + dfs(i+1,subsum-nums[i])

        return dfs(0,0)

    

        