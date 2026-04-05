class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumNums=sum(nums)
        n=len(nums)
        return  int((n*(n+1))//2 - sumNums)
        

        