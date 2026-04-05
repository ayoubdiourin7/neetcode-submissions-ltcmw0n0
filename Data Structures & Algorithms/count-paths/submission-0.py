class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m-1
        COLS = n-1


        def dfs(i,j):
            if i == ROWS or j == COLS :
                return 1
            return dfs(i+1,j)+dfs(i,j+1)
        return dfs(0,0)
        