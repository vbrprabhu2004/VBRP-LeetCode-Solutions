class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev1 = 0  # max up to i-2
        prev2 = 0  # max up to i-1

        for i in range(len(nums)):
            temp = prev2
            prev2 = max(prev1 + nums[i], prev2)
            prev1 = temp

        return prev2
