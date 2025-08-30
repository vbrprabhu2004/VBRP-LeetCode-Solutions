class Solution(object):
    def reverseWords(self, s):
        words = s.strip().split()
        words.reverse()
        return " ".join(words)