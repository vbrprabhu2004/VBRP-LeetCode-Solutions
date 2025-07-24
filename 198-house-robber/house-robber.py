class Solution(object):
    def rob(self, nums):

        prev1 = 0  # max up to i-2
        prev2 = 0  # max up to i-1

        for i in range(len(nums)):
            temp = prev2
            prev2 = max(prev1 + nums[i], prev2)
            prev1 = temp

        return prev2
''' My understanding code

class Solution(object):
    def rob(self, nums):

        even_sum, odd_sum = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum += nums[i]
            else:
                odd_sum += nums[i]
        return max(even_sum, odd_sum)
'''
