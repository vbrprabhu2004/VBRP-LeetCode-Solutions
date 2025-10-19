class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        if not matrix:
            return []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while left <= right and top <= bottom:

            # Left to Right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Top to Bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Right to Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # Bottom to Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res