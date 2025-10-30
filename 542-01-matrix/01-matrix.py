from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        
        # Initialize result matrix with large numbers
        res = [[99999 for _ in range(n)] for _ in range(m)]
        q = deque()
        
        # Step 1: Push all 0 cells into queue and set distance 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    q.append((i, j))
        
        # Directions → up, down, left, right
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 2: BFS traversal
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # Check bounds
                if 0 <= nx < m and 0 <= ny < n:
                    # If we found shorter distance
                    if res[nx][ny] > res[x][y] + 1:
                        res[nx][ny] = res[x][y] + 1
                        q.append((nx, ny))
        
        return res
