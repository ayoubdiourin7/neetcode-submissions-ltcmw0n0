class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        maxwater=0
        while l<r:
            maxwater = max(maxwater , (r-l)*min(h[r],h[l]))
            if h[l]<h[r] :
                l+=1
            else:
                r-=1
        return maxwater




        