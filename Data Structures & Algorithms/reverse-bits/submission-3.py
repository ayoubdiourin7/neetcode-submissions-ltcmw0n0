class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(31,-1,-1) :
            rest=n%2
            res+=(2**i)*rest
            i-=1
            n=n//2

        return res

        

        