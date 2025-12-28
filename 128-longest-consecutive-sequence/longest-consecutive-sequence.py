class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        l = 1
        final  = 1
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                l += 1
            elif nums[i-1] == nums[i]:
                l += 0
            else:
                l = 1
            final = max(final, l)
        return final