class Solution:
    def reverseBits(self, n: int) -> int:
        i=31
        res=0
        while n :
            rest=n%2
            res+=(2**i)*rest
            i-=1
            n=n//2

        return res

        

        