class Solution(object):
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        n = len(s)

        # dp[i] = True if s[:i] can be segmented into words from wordDict
        dp = [False] * (n + 1)
        dp[0] = True  # empty string is always valid

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]
