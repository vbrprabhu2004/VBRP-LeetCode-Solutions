class Solution(object):
    def nextGreaterElements(self, nums):
        
        n = len(nums)
        res = [-1] * n  
        stack = [] 

        for i in range(2 * n):
            num = nums[i % n]
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            if i < n:
                stack.append(i)
        return res
