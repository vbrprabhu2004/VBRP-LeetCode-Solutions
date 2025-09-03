class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        
        sum1 = 1  # 1 is always a divisor
        i = 2
        while i * i <= num:
            if num % i == 0:
                sum1 += i
                if i != num // i:  # avoid adding square root twice
                    sum1 += num // i
            i += 1
        
        return sum1 == num
