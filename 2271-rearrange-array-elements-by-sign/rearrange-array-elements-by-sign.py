class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        pos = []  
        neg = []  
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        for i in range(len(nums) // 2):
            nums[i * 2] = pos[i]  
            nums[i * 2 + 1] = neg[i] 
        return nums