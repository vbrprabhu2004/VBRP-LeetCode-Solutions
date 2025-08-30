class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        mapST, mapTS = {}, {}

        for ch_s, ch_t in zip(s, t):
            if ch_s in mapST and mapST[ch_s] != ch_t:
                return False
            if ch_t in mapTS and mapTS[ch_t] != ch_s:
                return False
            mapST[ch_s] = ch_t
            mapTS[ch_t] = ch_s

        return True
