class Solution(object):
    def minAddToMakeValid(self, s):

        open = 0 # Counts '(' unmatched
        add = 0  # Counts ')' unmatched

        for char in s:
            if char == '(':
                open += 1
            elif char == ')':
                if open > 0:
                    open -= 1 # match with an open '('
                else:
                    add += 1  # unmatched ')', need to add '('

        return open + add