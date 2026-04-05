class Solution:
    def climbStairs(self, n: int) -> int:
        
        pre=1
        prepre=1
        i=2
        while i <= n:
            res=pre+prepre
            pre,prepre = res,pre
            i+=1

        return pre
        


        