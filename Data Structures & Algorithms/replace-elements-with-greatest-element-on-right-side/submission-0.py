class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[-1]*len(arr)
        currMax=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            res[i]= currMax
            currMax = max(arr[i],currMax)
        return res
        