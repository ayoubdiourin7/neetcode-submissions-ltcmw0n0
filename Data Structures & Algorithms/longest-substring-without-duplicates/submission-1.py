class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)<=1 :
            return len(s)
        l,r=0,1
        unique=set(s[l])
        res=0
        while r<len(s):
            if s[r] in unique:
                unique.remove(s[l])
                l+=1
            else:
                unique.add(s[r])
                r+=1
                res=max(res,len(unique))
        return res
            

        