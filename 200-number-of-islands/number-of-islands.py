from collections import deque

class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        count = 0

        def bfs(queue):
            while queue:
                a, b = queue.popleft()

                if b + 1 < cols and grid[a][b+1] == "1":
                    grid[a][b+1] = "0"
                    queue.append((a, b+1))

                if a + 1 < rows and grid[a+1][b] == "1":
                    grid[a+1][b] = "0"
                    queue.append((a+1, b))

                if b - 1 >= 0 and grid[a][b-1] == "1":
                    grid[a][b-1] = "0"
                    queue.append((a, b-1))

                if a - 1 >= 0 and grid[a-1][b] == "1":
                    grid[a-1][b] = "0"
                    queue.append((a-1, b))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    grid[i][j] = "0"      # mark visited
                    queue.append((i, j))
                    bfs(queue)
                    count += 1

        return count
