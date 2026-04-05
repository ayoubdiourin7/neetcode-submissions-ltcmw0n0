class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        if  jump >= len(nums)-1:
            return True
        elif jump==0:
            return False
        reachLastIndex=False
        while jump > 0 and not reachLastIndex :
            reachLastIndex = self.canJump(nums[jump:])
            jump =jump-1

        return reachLastIndex

        
        

        