class Solution:
    def countSubstrings(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            j=1
            while j<=i and i+j<len(s):
                
                if s[i+j]==s[i-j]:
                    res+=1
                    j+=1
                else:
                    break
            
            j=1 
            while j<=i and i+j<=len(s):
                
                if s[i+j-1]==s[i-j]:
                    res+=1
                    j+=1
                else:
                    break
        

        return res+len(s)


        