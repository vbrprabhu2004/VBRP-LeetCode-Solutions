class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_element = float('inf')
        for i in range(len(nums)):
            if nums[i] < min_element:
                min_element = nums[i]
        return min_element