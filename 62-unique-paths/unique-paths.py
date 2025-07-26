class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Create a 2D DP table to store the number of unique paths
        # dp[i][j] will store the number of unique paths to reach cell (i, j)
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]

        # Initialize the first row and first column
        # There's only one way to reach any cell in the first row (by moving right)
        # There's only one way to reach any cell in the first column (by moving down)
        for i in xrange(m):
            dp[i][0] = 1
        for j in xrange(n):
            dp[0][j] = 1

        # Fill the DP table
        # For any cell (i, j), the number of unique paths to reach it
        # is the sum of unique paths from the cell above it (i-1, j)
        # and the cell to its left (i, j-1)
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # The bottom-right cell contains the total number of unique paths
        return dp[m-1][n-1]