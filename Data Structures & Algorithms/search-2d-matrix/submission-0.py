class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(m),len(m[0])


        top,bot=0,ROWS-1
        while top <= bot:
            row = (top+bot)//2

            if target < m[row][0]:
                bot=row-1
            elif m[row][-1] < target:
                top=row+1
            else:
                break
        
        if not (top <= bot):
            return False
        
        l,r=0,COLS-1
        while l <= r:
            mid = (l+r)//2

            if target < m[row][mid]:
                r=mid-1
            elif m[row][mid] < target:
                l=mid+1
            else:
                return True
        return False

            
        