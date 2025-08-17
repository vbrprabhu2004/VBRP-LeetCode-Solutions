class Solution(object):
    def findTargetSumWays(self, nums, target):
        memo = {}
        
        def dfs(i, total):
            # Base case: if we used all numbers
            if i == len(nums):
                return 1 if total == target else 0

            # Memoization check
            if (i, total) in memo:
                return memo[(i, total)]

            # Choose + or - for nums[i]
            add = dfs(i + 1, total + nums[i])
            sub = dfs(i + 1, total - nums[i])

            memo[(i, total)] = add + sub
            return memo[(i, total)]

        return dfs(0, 0)
