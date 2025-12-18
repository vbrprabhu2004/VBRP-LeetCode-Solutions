class Solution:
    def totalScore(self, hp: int, loss: List[int], need: List[int]) -> int:
        need = need[::-1]
        pref = list(accumulate(reversed(loss)))
        ans = 0
        for i in range(len(need)):
            x = hp - need[i]
            if i: x += pref[i - 1]
            ans += max(0, bisect_right(pref, x) - i)
        return ans