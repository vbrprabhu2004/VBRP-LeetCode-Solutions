class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        m = []
        n = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    m.append(i)
                    n.append(j)

        """
        for i in range(rows):
            for j in range(cols):
                if i in m or j in n:
                    matrix[i][j] = 0
        """
        for i in m:
            for j in range(cols):
                matrix[i][j] = 0
        
        for i in n:
            for j in range(rows):
                matrix[j][i] = 0