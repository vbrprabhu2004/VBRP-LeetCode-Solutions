class Solution(object):
    def canJump(self, nums):
        
        max_reach = 0  # farthest index we can reach
        n = len(nums)
        
        for i in range(n):
            if i > max_reach:
                return False  # if current index is not reachable
            max_reach = max(max_reach, i + nums[i])  # update max reach
            
            if max_reach >= n - 1:
                return True  # if we can reach or cross last index
                
        return True
