class Solution(object):
    def generate(self, numRows):
        pascal = []
        row = []
        for i in range(numRows):
            row = []
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    pre_row = pascal[i-1]
                    row.append(pre_row[j] + pre_row[j-1])
            pascal.append(row)
        return pascal