class Solution(object):
    def findPeakGrid(self, mat):
        max_val = float('-inf')
        max_pos = [0, 0]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] > max_val:
                    max_val = mat[i][j]
                    max_pos = [i, j]
        
        return max_pos
