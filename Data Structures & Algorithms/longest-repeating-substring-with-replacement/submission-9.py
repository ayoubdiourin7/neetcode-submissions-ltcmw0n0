class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # idea is to find the most repeated char and replace other 
        # char n time  while    n<=k and calcule max of the curr
        #substring 

        count={}
        l=0
        maxCount=0
        res=0
        for r , char in enumerate(s):
            count[char]= count.get(char,0)+1
            maxCount = max(maxCount, count[char])

            while (r-l+1)- maxCount > k :
                count[s[l]] -= 1
                l+=1

            res = max(res, r - l + 1)

        return res





           

        return res

