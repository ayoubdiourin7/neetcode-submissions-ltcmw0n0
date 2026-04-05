class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cls = set()
        boxes = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "." :
                    continue
                digit=int(board[i][j])
                if ((digit,i) in rows ) or ((digit,j) in cls ) or ((digit,i//3,j//3) in boxes):
                    return False
                rows.add((digit,i))
                cls.add((digit,j))
                boxes.add((digit,i//3,j//3))
        return True 

                
                


        
        