class Solution(object):
    def repeatedStringMatch(self, a, b):
        count = 1
        repeated = a

        while len(repeated) < len(b):
            repeated += a
            count += 1
        
        if b in repeated:
            return count

        repeated += a
        count += 1
        if b in repeated:
            return count
        
        return -1
        