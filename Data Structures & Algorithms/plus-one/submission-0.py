class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=deque()
        carry=1
        for digit in digits[::-1]:
            temp=digit+carry
            if 10 <= temp:
                res.appendleft(0)
                carry=1
            else:
                res.appendleft(temp)
                carry=0
        if carry == 1:
            res.appendleft(carry)
            
        return list(res)
            
        