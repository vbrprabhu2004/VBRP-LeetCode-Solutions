class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        stack = [-1]

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxlen = max(maxlen, i - stack[-1])
        return maxlen