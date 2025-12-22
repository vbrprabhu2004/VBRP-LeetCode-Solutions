from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        ans = []
        
        def bfs(starts):
            visited = [[False] * cols for _ in range(rows)]
            queue = deque(starts)

            for r, c in starts:
                visited[r][c] = True
            
            while queue:
                a, b = queue.popleft()

                if b + 1 < cols and not visited[a][b+1] and heights[a][b + 1] >= heights[a][b]:
                    visited[a][b+1] = True
                    queue.append((a, b + 1))    

                if a + 1 < rows and not visited[a+1][b] and heights[a + 1][b] >= heights[a][b]:
                    visited[a+1][b] = True
                    queue.append((a + 1, b))

                if b - 1 >= 0 and not visited[a][b-1] and heights[a][b - 1] >= heights[a][b]:
                    visited[a][b-1] = True
                    queue.append((a, b - 1))
                    
                if a - 1 >= 0 and not visited[a-1][b] and heights[a - 1][b] >= heights[a][b]:
                    visited[a-1][b] = True
                    queue.append((a - 1, b))
        
            return visited

        pacific_starts = []
        atlantic_starts = []

        for i in range(rows):
            pacific_starts.append((i, 0))
            atlantic_starts.append((i, cols - 1))

        for j in range(cols):
            pacific_starts.append((0, j))
            atlantic_starts.append((rows - 1, j))
        
        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i,j])
        return ans