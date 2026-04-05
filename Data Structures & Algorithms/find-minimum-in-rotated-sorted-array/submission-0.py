class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        n=len(nums)
        while l<=r:
            m=(l+r)//2
            v=nums[m]
            aft=nums[(m+1)%n]
            bfr=nums[(m-1)%n]
            if v<=aft<=bfr:
                return v
            elif nums[r]>=nums[l]:
                return nums[l]
            elif v<=nums[r]:
                r=m-1
            else:
                l=m+1
        return -1



        