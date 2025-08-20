class Solution(object):
    def check(self, nums):
        result, n = 0, len(nums)
        for i in range(1, n):
            if nums[i] >= nums[i - 1]:
                result += 1

        if nums[0] >= nums[-1]:
            result += 1
            
        return result >= n-1