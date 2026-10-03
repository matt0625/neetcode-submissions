class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        for col in range(cols):
            if board[0][col] == "O": self.regionDFS(board, 0, col)
            if board[rows-1][col] == "O": self.regionDFS(board, rows-1, col)

        for row in range(rows):
            if board[row][0] == "O": self.regionDFS(board, row, 0)
            if board[row][cols-1] == "O": self.regionDFS(board, row, cols-1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"

                elif board[r][c] == "O":
                    board[r][c] = "X"       


    def regionDFS(self, board, r, c):
        drc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        if board[r][c] != "O":
            return
        
        board[r][c] = "#"

        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            
            if nr < 0 or nc < 0 or nr >= len(board) or nc >= len(board[0]):
                continue

            else:
               self.regionDFS(board, nr, nc)
