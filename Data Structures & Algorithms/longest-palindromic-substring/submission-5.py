class Solution:
    def longestPalindrome(self, s: str) -> str:

    
        n=len(s)
        maxlen=0
        res=s[0]
        for i in range(0,n):
            for j in range(n-1,i,-1):
                
                sub=s[i:j+1]
                print(sub)
                if sub  == sub[::-1] and maxlen<j-i+1:
                    res=sub
                    maxlen=j-i+1


        return res

                    
                    


        