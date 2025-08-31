class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack