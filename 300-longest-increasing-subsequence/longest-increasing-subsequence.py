class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        # dp[i] = length of LIS ending at index i
        dp = [1] * n

        # Build the dp array
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # The longest subsequence length is the maximum in dp[]
        return max(dp)
