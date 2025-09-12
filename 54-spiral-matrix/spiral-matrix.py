class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        res = []
        while matrix:
            # 1. Take the first row
            res += matrix.pop(0)
            
            # 2. Take the last column
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            
            # 3. Take the last row reversed
            if matrix:
                res += matrix.pop()[::-1]
            
            # 4. Take the first column reversed
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        
        return res
