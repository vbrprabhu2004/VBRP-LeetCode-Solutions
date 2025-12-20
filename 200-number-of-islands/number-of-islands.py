class Solution:
    

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid) #rows
        m = len(grid[0]) #cols
        visited = [[False for i in range(m)] for j in range(n)]
        cnt = 0

        def dfs(grid, visited, n, m, i, j):
            if i<0 or i>=n or j<0 or j>=m:
                return
            if grid[i][j] == "0":
                return
            if visited[i][j] == True:
                return
            
            visited[i][j] = True

            dfs(grid, visited, n, m , i+1, j)
            dfs(grid, visited, n, m , i, j+1)
            dfs(grid, visited, n, m , i-1, j)
            dfs(grid, visited, n, m , i, j-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and visited[i][j] == False:
                    dfs(grid, visited, n, m , i, j)
                    cnt += 1
        #print(visited)
        return cnt