class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS , COLS = len(board) , len(board[0])
        path = set()
        def dfs(i,j,word):

            if not word:
                return True
            c = word[0]
            if (i<0 or j < 0 or i >= ROWS or j >= COLS ) or not (c==board[i][j]) or (i,j) in path:
                return False

            path.add((i,j))
            res =dfs(i+1,j,word[1:]) or dfs(i,j+1,word[1:]) or dfs(i-1,j,word[1:]) or dfs(i,j-1,word[1:])
            path.remove((i,j))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, word):
                    return True
        return False


            

            


        