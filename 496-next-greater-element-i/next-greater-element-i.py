class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        final = []

        for i in nums1:
            index = nums2.index(i)  # Get the index of i in nums2
            next_greater = -1       

            for j in range(index + 1, len(nums2)):
                if nums2[j] > i:
                    next_greater = nums2[j]
                    break

            final.append(next_greater)

        return final
