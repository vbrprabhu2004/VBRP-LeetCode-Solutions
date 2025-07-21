''' Understood by me
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n < k:
            return []

        result = []

        # Compute max for first window
        window_max = max(nums[:k])
        result.append(window_max)

        # Slide the window
        for i in range(k, n):
            # New window: nums[i-k+1 to i]
            window = nums[i - k + 1 : i + 1]
            window_max = max(window)
            result.append(window_max)

        return result
    '''
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if not nums or k == 0:
            return []
        
        result = []
        dq = deque()  # Store indices of useful elements

        for i in range(n):
            # Remove elements outside the window from the front
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Append max to result once we have a complete window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result