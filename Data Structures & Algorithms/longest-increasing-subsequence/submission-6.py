class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i,j):

            if i<0:
                return 0
            if j==-1 or nums[i]<nums[j] :
                return max(1+dfs(i-1, i) ,dfs(i-1, j))

            return dfs(i-1, j)
            
            
        return dfs(len(nums)-1,-1)

            

                





        