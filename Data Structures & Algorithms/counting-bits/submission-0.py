class Solution:
    def countBits(self, n: int) -> List[int]:
        def coutBit(num):
            sumBite=0
            while num:
                sumBite+=num%2
                num=num//2
            return sumBite
        return list(map(coutBit, range(n+1)))
        