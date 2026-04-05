class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightpro = [1]*len(nums)
        leftpro = [1]*len(nums)
        res=[1]*len(nums)

        for i in range(1,len(nums)):
            rightpro[i]=rightpro[i-1]*nums[i-1]
        
        for i in  range(len(nums)-2,-1,-1):
            leftpro[i]=leftpro[i+1]*nums[i+1]


        for i in range(len(nums)):
            res[i]=leftpro[i]*rightpro[i]

        return res




        