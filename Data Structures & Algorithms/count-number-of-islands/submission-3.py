class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands += 1
                    self.dfs(grid, r, c)

        return islands 


    def dfs(self, grid, r, c):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return
        
        if grid[r][c] == "0":
            return 

        grid[r][c] = "0"

        drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        for dr, dc in drc:
            self.dfs(grid, r+dr, c+dc)



