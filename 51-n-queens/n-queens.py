class Solution(object):
    def solveNQueens(self, n):
        def backtrack(row, cols, pos_diags, neg_diags, board):
            if row == n:
                result.append([''.join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                pos_diags.add(row + col)
                neg_diags.add(row - col)

                backtrack(row + 1, cols, pos_diags, neg_diags, board)

                board[row][col] = '.'
                cols.remove(col)
                pos_diags.remove(row + col)
                neg_diags.remove(row - col)

        result = []
        empty_board = [['.'] * n for _ in range(n)]  
        backtrack(0, set(), set(), set(), empty_board)
        return result
