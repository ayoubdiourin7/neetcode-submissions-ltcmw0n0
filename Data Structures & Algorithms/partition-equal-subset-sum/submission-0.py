class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def dfs(i , sub1,sub2):

            if i == len(nums):
                return sub1==sub2

            if dfs(i+1,sub1+nums[i],sub2) :
                return True
            if dfs(i+1,sub1,sub2+nums[i]) :
                return True
            
            return False

        return dfs(0,0,0)
        

        
            

