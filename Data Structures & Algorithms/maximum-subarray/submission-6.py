class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      # unserstand what been ask 
        curSum = 0
        res=nums[0]
 

        for i in range(len(nums)):
            if nums[i]> curSum and curSum<0 :
                curSum=nums[i]
                res=max(nums[i],res)

            else:
                res=max(curSum +nums[i],res)
                curSum=curSum +nums[i]
            
        return res
            


        