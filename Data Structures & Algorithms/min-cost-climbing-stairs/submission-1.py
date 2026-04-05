class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost={}

        def dfs(i):
            if len(cost)<=i:
                return 0
            if not i in mincost:
                mincost[i]=cost[i]+min(dfs(i+1),dfs(i+2))
            
            return mincost[i]
        
        return min(dfs(0),dfs(1))
        