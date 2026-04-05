class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            midi = (left+right)//2
            midv = nums[midi]
            if midv == target:
                return midi
            elif target < midv:
                right=midi-1
            else:
                left=midi+1

        return -1
        