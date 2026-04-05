class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxdif=0
        while r<len(prices):
            if prices[l] < prices[r]:
                maxdif=max(prices[r] -prices[l],maxdif)
            else:
                l=r
            r+=1   
        return maxdif

        