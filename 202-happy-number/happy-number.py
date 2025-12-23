class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False   # cycle detected
            
            seen.add(n)
            sums = 0

            while n > 0:
                rem = n % 10
                sums += rem * rem
                n = n // 10

            n = sums

        return True
