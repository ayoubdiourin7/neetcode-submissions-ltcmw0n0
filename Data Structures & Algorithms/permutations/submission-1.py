class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        result = []
        stack=[]
        def dfs(nums,res):
            
            if not nums:
                result.append(res)
                return 
            for j in range(len(nums)):
                dfs(nums[:j]+nums[j+1:] , res + [nums[j]])
            return 
        print(dfs(nums , []))
        return result
                    



        