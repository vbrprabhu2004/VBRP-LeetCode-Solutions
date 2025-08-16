class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        min_sum, sum1 = 0, 0
        rows = len(grid)
        cols = len(grid[0])
        matrix = [[0 for j in range(cols)] for i in range(rows)]
        matrix[0][0] = grid[0][0]

        for i in range(0, rows):
            for j in range(0, cols):
                if i==0 and j==0:
                    continue
                else:
                    if i==0:
                        matrix[i][j] = grid[i][j] + matrix[i][j-1]
                    elif j==0:
                        matrix[i][j] = grid[i][j] + matrix[i-1][j]
                    else:
                        matrix[i][j] = grid[i][j] + min(matrix[i-1][j], matrix[i][j-1])
        
        
        return matrix[rows-1][cols-1]
        '''
        for j in range(1, cols):
            matrix[0][j] = matrix[0][j-1] + grid[0][j]
        for i in range(1, rows):
            matrix[i][0] = matrix[i-1][0] + grid[i][0]
        '''