class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub = {}
        sub[0]=1
        subsum =0
        res=0



        for e in nums:
            subsum+=e
            
            res+=sub.get(subsum-k,0)
            sub[subsum]=1+sub.get(subsum,0)
            
        #res+=sub.get(0,0)
        return res
        