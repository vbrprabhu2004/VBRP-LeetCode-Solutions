class Solution(object):
    def convertToTitle(self, columnNumber):
        res=[]
        while columnNumber > 0:
            columnNumber -=1
            r = columnNumber %26
            res.append(chr(ord('A')+r))
            columnNumber //=26
        return ''.join(reversed(res))
        