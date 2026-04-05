class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l <= r:
            lv=nums[l]
            rv=nums[r]
            m=(l+r)//2
            mv=nums[m]
            if target == mv :
                return m
            if lv<=mv:
                if lv <= target <= mv :
                    r=m-1
                else:
                    l=m+1
            else:
                if mv<=target<=rv :
                    l=m+1
                else:
                    r=m-1

        return -1


        