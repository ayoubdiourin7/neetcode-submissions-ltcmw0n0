class Solution:
    def romanToInt(self, s: str) -> int:
        su=0
        n=len(s)
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        for i in range(n):

            if i+1<=n-1 and roman[s[i]] < roman[s[i+1]]  :
                su-=roman[s[i]]
            else:
                su+=roman[s[i]]

        return su



        