class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0

        def check(i,j):
            if j==len(grid[0]) or i ==len(grid) or j==-1 or i==-1 or grid[i][j]=="0":
                return 
            grid[i][j]="0"
            check(i-1,j)
            check(i+1,j)
            check(i,j+1)
            check(i,j-1)
            

             


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if  grid[i][j]=="1":
                    res+=1
                    check(i,j)
        return res

                
        