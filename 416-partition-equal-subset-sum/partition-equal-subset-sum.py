''' My understanding code
class Solution(object):
    def canPartition(self, nums):
        if not nums:
            return False
        
        max_element = max(nums)
        return max_element == sum(nums) - max_element
'''
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        # If total sum is odd, cannot split into two equal subsets
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        # DP array to check if a sum is possible
        dp = [False] * (target + 1)
        dp[0] = True  # Sum 0 is always possible

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
