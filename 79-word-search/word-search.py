class Solution(object):
    def exist(self, board, word):
        if not board or not board[0]:
            return False

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = "#"  # mark visited

            found = (dfs(r+1, c, index+1) or
                     dfs(r-1, c, index+1) or
                     dfs(r, c+1, index+1) or
                     dfs(r, c-1, index+1))

            board[r][c] = temp  # restore cell
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
