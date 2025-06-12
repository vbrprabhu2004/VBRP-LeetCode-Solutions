class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums_S = sorted(nums)
        n = len(nums_S)

        if n % 2 != 0:
            index = (n + 1) // 2
            return float(nums_S[index - 1])  
        else:
            index1 = n // 2
            index2 = (n // 2) + 1
            return (nums_S[index1 - 1] + nums_S[index2 - 1]) / 2.0  
