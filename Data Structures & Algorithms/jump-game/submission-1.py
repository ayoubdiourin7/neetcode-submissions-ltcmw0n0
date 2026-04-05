class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        count=1
        for i in range(len(nums)-2 , -1 , -1):
            if count > nums[i]:
                count+=1
            else:
                count=1
        return count == 1



        
        

        