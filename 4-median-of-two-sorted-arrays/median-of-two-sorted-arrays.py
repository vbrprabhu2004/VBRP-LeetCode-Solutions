class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = (nums1 + nums2)
        result.sort()
        x = len(result)
        small = 0
        large = x-1
        for i in range(x):
            mid = (small + large) // 2
            if x % 2 != 0:
                return result[mid]
            else:
                return (result[mid] + result[mid + 1]) / 2