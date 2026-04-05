class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m-1
        COLS = n-1
        path={}


        def dfs(i,j):
            if i == ROWS or j == COLS :
                return 1
            if (i,j) not in path :
                path[(i,j)]=dfs(i+1,j)+dfs(i,j+1)
            return path[(i,j)]
        return dfs(0,0)
        