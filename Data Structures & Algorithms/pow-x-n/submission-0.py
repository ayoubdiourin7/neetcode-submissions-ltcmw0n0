class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        i=0

        while i<abs(n):
            res*=x
            i+=1

        return res if 0<n else 1/res

        