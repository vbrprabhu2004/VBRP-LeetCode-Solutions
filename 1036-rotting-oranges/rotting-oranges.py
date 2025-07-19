from collections import deque

class Solution(object):
    def orangesRotting(self, grid):

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Initialize the queue with all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        time = 0
        
        # BFS to rot adjacent fresh oranges
        while queue:
            r, c, t = queue.popleft()
            time = max(time, t)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, t + 1))
        
        return time if fresh == 0 else -1
