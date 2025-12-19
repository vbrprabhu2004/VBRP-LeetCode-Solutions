class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        maxi = 0
        temp = -1
        seen = {}
        for i in range(len(s)):
            if s[i] not in seen.keys():
                seen[s[i]] = i
                cnt += 1
            else:
                if seen[s[i]] > temp:
                    cnt = i - seen[s[i]]
                    temp = seen[s[i]]
                else:
                    cnt += 1
                seen[s[i]] = i
            maxi = max(maxi, cnt)
        return maxi