class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        list1 = [i for i in range(0, size + 1)]
        nums.sort()
        missing = (set(list1) - set(nums)).pop()
        return missing