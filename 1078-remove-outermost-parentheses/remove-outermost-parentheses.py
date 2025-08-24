class Solution(object):
    def removeOuterParentheses(self, s):
        res, bal = [], 0
        for ch in s:
            if ch == '(':
                if bal > 0: res.append(ch)
                bal += 1
            else:
                bal -= 1
                if bal > 0: res.append(ch)
        return "".join(res)