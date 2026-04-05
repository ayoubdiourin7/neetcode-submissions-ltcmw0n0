class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            j=1
            while j<=i and i+j<len(s) and s[i+j]==s[i-j]:
                    res+=1
                    j+=1

            
            j=1 
            while j<=i and i+j<=len(s) and s[i+j-1]==s[i-j] :
                    res+=1
                    j+=1

        

        return res+len(s)


        