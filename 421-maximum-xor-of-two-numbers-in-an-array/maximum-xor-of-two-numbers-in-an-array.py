''' My understanding code
class Solution(object):
    def findMaximumXOR(self, nums):
        max_xor = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                max_xor = max(max_xor, nums[i] ^ nums[j])
        return max_xor
'''
class Solution(object):
    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0

        for i in range(31, -1, -1):  # Check each bit from highest to lowest
            mask |= (1 << i)
            prefixes = set()

            for num in nums:
                prefixes.add(num & mask)

            # Try to set current bit in max_xor to 1
            temp = max_xor | (1 << i)

            # Check if there exists two prefixes a and b such that a ^ b = temp
            for prefix in prefixes:
                if (temp ^ prefix) in prefixes:
                    max_xor = temp
                    break

        return max_xor
