class Solution(object):
    def subarraysWithKDistinct(self, nums, k):

        def atMostK(nums, k):
            count = {}
            res = i = 0
            for j in range(len(nums)):
                if nums[j] not in count or count[nums[j]] == 0:
                    k -= 1
                count[nums[j]] = count.get(nums[j], 0) + 1
                while k < 0:
                    count[nums[i]] -= 1
                    if count[nums[i]] == 0:
                        k += 1
                    i += 1
                res += j - i + 1
            return res

        return atMostK(nums, k) - atMostK(nums, k - 1)
