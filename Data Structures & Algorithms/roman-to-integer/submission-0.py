class Solution:
    def romanToInt(self, s: str) -> int:
        su=0
        n=len(s)
        roman = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500, "M": 1000
        }

        for i in range(n):

            if s[i] == "I" and i < n-1 and s[i+1] in ("V" , "X"):
                su-=roman["I"] 
            elif s[i] == "X" and i < n-1 and s[i+1] in ("L" , "C"):
                su-=roman["X"]
            elif s[i] == "C" and i < n-1 and s[i+1] in ("D" , "M"):
                su-=roman["C"]
            else:
                su+=roman[s[i]]

        return su



        