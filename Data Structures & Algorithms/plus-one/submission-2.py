class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=[]
        carry=1
        digits.reverse()
        for digit in digits:
            temp=digit+carry
            if 10 <= temp:
                res.append(0)
                carry=1
            else:
                res.append(temp)
                carry=0
        if carry == 1:
            res.append(carry)
        res.reverse() 
        return res
            
        