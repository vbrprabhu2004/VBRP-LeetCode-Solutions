import math
class Solution(object):
    def convert(self, s, numRows):
        l = len(s)
        c = 2*(numRows-1)
        count = 0
        res=""
        if numRows==1:
            return s
        for i in range(numRows):
            if i==0 or i==numRows-1:
                a=i
                while a<l:
                    res+=s[int(a)]
                    a+=c
                count+=1
            else:
                a=i
                while a<l:
                    res+=s[int(a)]
                    if a+(c-2*i)<l:
                        res+=s[int(a+(c-2*i))]

                    a+=c
                count+=1

        return res                          