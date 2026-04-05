class Solution:
    def numDecodings(self, s: str) -> int:
        count={}
        def dfs(i):
            if i>=len(s):
                return 1
            if i in count:
                return count[i]
            if "0"==s[i]:
                count[i]=0
                return 0

            if i+1<len(s) and int(s[i:i+2])<=26:
                count[i]=dfs(i+1)+dfs(i+2)
                return count[i]
            count[i]=dfs(i+1)
            return count[i]
        
        return dfs(0)

            

            
            






        '''253728

        2 5 3 7 2 8
        25 x
        25
        25 3 7 2 8'''
        