class Solution:
    def hammingWeight(self, n: int) -> int:
        sumBite=0
        while n:
            n &= n - 1
            sumBite+=1
        return sumBite


        