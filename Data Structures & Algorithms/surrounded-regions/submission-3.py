class Solution:
    def solve(self, board: List[List[str]]) -> None:

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        ROW = len(board) 
        COL = len(board[0]) 

        def Oedge(row, col):
            if board[row][col] != 'O':
                return
            board[row][col] = 'T'
            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if nr < 0 or nr >= ROW or nc < 0 or nc >= COL: #outofbound
                    continue
                if board[nr][nc] == 'O': # for all connected 'O's
                    Oedge(nr, nc) 

        for r in range(ROW):
            Oedge(r, 0) # left side
            Oedge(r, COL-1) #right side
        
        for c in range(COL):
            Oedge(0, c) #top
            Oedge(ROW-1, c) #bottom

        for i in range(0, ROW):
            for j in range(0, COL):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'
        