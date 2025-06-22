class Solution(object):
    def divideString(self, s, k, fill):
        res=[]

        for i in range(0,len(s),k):
            temp=s[i:i+k]

            if len(temp)<k:
                temp+=fill*(k-len(temp))
            res.append(temp)
        return res

        