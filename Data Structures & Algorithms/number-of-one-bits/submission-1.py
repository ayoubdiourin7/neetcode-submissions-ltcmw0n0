class Solution:
    def hammingWeight(self, num: int) -> int:
        sumBite=0
        while num:
            sumBite+=num%2
            num>>=1
        return sumBite


        