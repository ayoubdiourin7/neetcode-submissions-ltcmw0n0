class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        dic=set()
        res=0
        for num in nums:
            dic.add(num)

        
        for num in nums:
            if not (num-1 in dic):
                lencon=1
                currnum=num+1
                while currnum in dic:
                    lencon+=1
                    currnum+=1
                res=max(res,lencon)
        return res


        