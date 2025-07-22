class Solution(object):
    def numberOfSubstrings(self, s):

        last_seen = [-1, -1, -1]
        res = 0

        for i in range(len(s)):
            last_seen[ord(s[i]) - ord('a')] = i

            if -1 not in last_seen:
                res += min(last_seen) + 1

        return res
