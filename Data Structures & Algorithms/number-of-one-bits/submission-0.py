class Solution:
    def hammingWeight(self, num: int) -> int:
        sumBite=0
        while not (num == 0):
            rest=num%2
            num=num//2
            sumBite+=rest
        return sumBite


        