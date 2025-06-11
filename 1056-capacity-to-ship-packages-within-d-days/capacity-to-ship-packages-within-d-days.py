class Solution(object):
    def shipWithinDays(self, weights, days):

        left = max(weights)
        right = sum(weights)

        def isValid(w):
            total = 0
            count = 1
            for i in weights:
                if total + i <= w:
                    total += i
                else:
                    total = i
                    count += 1
            return count <= days

        while left < right:
            mid = (left + right) // 2
            if isValid(mid):
                right = mid
            else:
                left = mid + 1

        return left