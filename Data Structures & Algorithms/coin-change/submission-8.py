class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        targets={}
        coins=sorted(coins,reverse=True )


        def dfs(target):
            if target<0 :
                return float("inf")
            if target == 0:
                return 0
            if target in targets:
                return targets[target]

            rest=float("inf")
            for coin in coins:
                rest = min(rest,1+dfs(target-coin))
            targets[target] = rest
            return rest
        res = dfs(amount)

        return res if res != float("inf") else -1

        '''dp=[amount + 1]*(amount+1)
        dp[0]=0

        for target in range(1,amount+1):
            for coin in coins:
                if target-coin>=0:
                    dp[target]=min(dp[target],1+dp[target-coin])'''
            


        




        




    
   