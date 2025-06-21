class Solution(object):
    def beautySum(self, s):
        n = len(s)
        Total = 0

        for i in range(n):
            freq = {}
            Max = float("-inf")
            for j in range(i, n):
                char = s[j]
                freq[char] = freq.get(char,0) + 1
                Max = max(Max, freq[char])
                Min = min(freq.values())
                Total += Max - Min
        return Total