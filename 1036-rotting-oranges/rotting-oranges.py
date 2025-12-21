from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        count = 0
        time = 0

        def bfs(queue, size, time):
            while queue:
                a, b = queue.popleft()
                size -= 1
                
                if a + 1 <= rows - 1 and grid[a + 1][b] == 1:
                    grid[a + 1][b] = 2
                    queue.append((a + 1, b))

                if a - 1 >= 0 and grid[a - 1][b] == 1:
                    grid[a - 1][b] = 2
                    queue.append((a - 1, b))

                if b + 1 <= cols - 1 and grid[a][b + 1] == 1:
                    grid[a][b + 1] = 2
                    queue.append((a, b + 1))

                if b - 1 >= 0 and grid[a][b - 1] == 1:
                    grid[a][b - 1] = 2
                    queue.append((a, b - 1))
                
                if size == 0:
                    time += 1
                    #print(time, queue)
                    size += len(queue)

            return time - 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))

        size = len(queue)
        #print(size)
        while queue:
            time = bfs(queue, size, time)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1: 
                    return -1           
        return time