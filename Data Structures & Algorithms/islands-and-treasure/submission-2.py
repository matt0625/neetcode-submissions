from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue:
            r, c = queue.popleft()

            for dr, dc in drc:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] != 2147483647:
                    continue
                
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))


        
