class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res=0

        def check(i,j):
            nonlocal seen 
            if j==len(grid[0]) or i ==len(grid) or j==-1 or i==-1:
                return 
            if not (i,j) in seen and grid[i][j]=="1":
                seen.add((i,j))
                check(i-1,j)
                check(i+1,j)
                check(i,j+1)
                check(i,j-1)

            return 


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not (i,j) in seen and grid[i][j]=="1":
                    res+=1
                    check(i,j)
        return res

                
        