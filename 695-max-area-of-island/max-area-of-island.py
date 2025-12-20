from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #curr_area = 0
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        def bfs(queue):
            curr_area = 0
            while queue:
                a, b = queue.popleft()
                #print(a,b)
                curr_area += 1

                if b + 1 < cols and grid[a][b+1] == 1:
                    grid[a][b+1] = 0
                    queue.append((a, b+1))

                if a + 1 < rows and grid[a+1][b] == 1:
                    grid[a+1][b] = 0
                    queue.append((a+1, b))

                if b - 1 >= 0 and grid[a][b-1] == 1:
                    grid[a][b-1] = 0
                    queue.append((a, b-1))

                if a - 1 >= 0 and grid[a-1][b] == 1:
                    grid[a-1][b] = 0
                    queue.append((a-1, b))
            return curr_area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0      # mark visited
                    queue.append((i, j))
                    curr_area = bfs(queue)               
                    max_area = max(max_area, curr_area)  
        return max_area
