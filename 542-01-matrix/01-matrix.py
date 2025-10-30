class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        INF = 99999

        # Step 1: Create result matrix
        res = [[INF for _ in range(n)] for _ in range(m)]

        # Step 2: First pass → Top-Left to Bottom-Right
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i][j], res[i - 1][j] + 1)
                    if j > 0:
                        res[i][j] = min(res[i][j], res[i][j - 1] + 1)

        # Step 3: Second pass → Bottom-Right to Top-Left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    res[i][j] = min(res[i][j], res[i + 1][j] + 1)
                if j < n - 1:
                    res[i][j] = min(res[i][j], res[i][j + 1] + 1)

        return res
