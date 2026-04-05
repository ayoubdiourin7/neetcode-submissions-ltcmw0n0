class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pre={}

        for i,num in enumerate(nums):
            if num in pre:
                return [pre[num],i]
            pre[target-num]=i


        