class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            stack = []

            j = 1
            while j * j <= num:
                if num % j == 0:
                    stack.append(j)
                    if j != num // j:
                        stack.append(num // j)

                if len(stack) > 4:   # early stop
                    break

                j += 1

            if len(stack) == 4:
                total += sum(stack)
        return total
''' MY CODE
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for i in range(len(nums)):
            stack = []   
            num = nums[i]

            for j in range(1, num + 1):
                if num % j == 0:
                    stack.append(j)

            if len(stack) == 4:
                total += sum(stack)

        return total
'''