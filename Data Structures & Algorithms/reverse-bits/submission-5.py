class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(31,-1,-1) :
            res+=(2**i)*(n%2)
            n=n//2

        return res

        

        