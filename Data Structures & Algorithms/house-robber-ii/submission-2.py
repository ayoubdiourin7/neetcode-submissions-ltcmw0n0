class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))

        
    def helper(self ,nums):
        n=len(nums)
        if not nums:
            return 0
        if n==1:
            return nums[0]
        first =nums[0]
        second =max(nums[0],nums[1])
        for i in range(2,n):
            temp=second
            second=max(second,first+nums[i])
            first = temp
        return second
    