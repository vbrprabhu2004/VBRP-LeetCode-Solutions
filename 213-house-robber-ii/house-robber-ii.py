class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            prev1 = 0
            prev2 = 0
            for num in arr:
                temp = prev1
                prev1 = max(prev2 + num, prev1)
                prev2 = temp
            return prev1

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
