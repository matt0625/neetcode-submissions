class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = self.dfsArea(grid, r, c)
                    maxArea = max(maxArea, area)

        return maxArea

    def dfsArea(self, grid, r, c):
        if (
            r < 0
            or c < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or grid[r][c] == 0
        ):
            return 0

        grid[r][c] = 0

        area = 1
        area += self.dfsArea(grid, r + 1, c)
        area += self.dfsArea(grid, r - 1, c)
        area += self.dfsArea(grid, r, c + 1)
        area += self.dfsArea(grid, r, c - 1)

        return area