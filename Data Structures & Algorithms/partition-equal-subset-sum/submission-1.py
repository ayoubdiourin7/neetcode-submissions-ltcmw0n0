class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sumNums=sum(nums)

        if not (sumNums % 2 == 0):
            return False

        def dfs(i , total):

            if i == len(nums):
                return total==0

            if dfs(i+1,total-nums[i]) :
                return True
            if dfs(i+1,total) :
                return True
            
            return False

        return dfs(0, sum(nums) // 2)
        

            

