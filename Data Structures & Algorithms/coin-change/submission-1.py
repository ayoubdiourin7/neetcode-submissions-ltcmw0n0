class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        targets={}

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


        




    
   