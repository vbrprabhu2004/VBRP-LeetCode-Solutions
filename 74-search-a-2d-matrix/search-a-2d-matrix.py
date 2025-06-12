class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for val in row:
                if target == val:
                    return True
        return False