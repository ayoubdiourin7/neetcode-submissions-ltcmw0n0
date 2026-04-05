from typing import List

class Solution:
    def rotate(self, mat: List[List[int]]) -> None:

        #rotate means (i,j)=>(j,n-1-i) means transpose Reverse each row

        #first  (i,j) become (n-1-i , j)
        n=len(mat)
        for i in range(n//2):
            for j in range(n):
                temp=mat[n-1-i][j]
                mat[n-1-i][j]=mat[i][j]
                mat[i][j]=temp

        #seconde (n-1-i , j) become (j,n-1-i)
        # means (i,j ) become (j,i)
        for i in range(n):
            for j in range(0,i+1):
                temp=mat[i][j]
                mat[i][j]=mat[j][i]
                mat[j][i]=temp
        
        