class Solution:
    def isHappy(self, n: int) -> bool:
        cycle=set()
        def helper(n):
            
            res=0
            while n!=0:
                res+=(n%10)**2
                print(res)

                n=n//10
            
            if res == 1:
                return True 

            
            if res in  cycle:
                return False 

            cycle.add(res)
            return helper(res)

        return helper(n)
            

        