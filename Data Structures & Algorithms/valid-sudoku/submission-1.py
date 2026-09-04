from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_seen = defaultdict(set)
        col_seen = defaultdict(set)
        grid_seen = defaultdict(set)
        grid_counter = 1

        for i in range(len(board)):
            if i < 3:
                grid_counter = 1
            elif i < 6:
                grid_counter = 4
            else:
                grid_counter = 7
            for j in range(len(board[i])):
                curr = board[i][j]
                if j % 3 == 0 and j != 0:
                    grid_counter += 1
                if curr == '.':
                    continue


                if curr in row_seen[i] or curr in col_seen[j]:
                    return False
                elif curr in grid_seen[grid_counter]:
                    return False
                
                row_seen[i].add(curr)
                col_seen[j].add(curr)
                grid_seen[grid_counter].add(curr)

        return True

