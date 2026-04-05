class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        pair = n%2 == 0

        maxlen=0
        res=s[0]
        for i in range(0,n):
            j=1

            while i+j<n and  i-j>=0 and s[i-j]==s[i+j] :            
                if  maxlen < 2*j+1:
                    res=s[i-j:i+j+1]
                    maxlen=2*j+1
                j+=1
            j=1
            while i+j<n and  i-j+1>=0 and s[i+j]==s[i-j+1] :            
                if  maxlen < 2*j:
                    res=s[i-j+1:i+j+1]
                    maxlen=2*j
                j+=1

        return res
            
            
            
                
















    '''def longestPalindrome(self, s: str) -> str:

    
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


        return res'''

                    
                    


        