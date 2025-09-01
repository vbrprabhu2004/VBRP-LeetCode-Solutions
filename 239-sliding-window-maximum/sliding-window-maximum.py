from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result = []
        dq = deque()   # store indices of useful elements

        for i in range(len(nums)):
            # 1. remove indices that are out of this window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # 2. remove smaller values (they are useless)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. add current index
            dq.append(i)

            # 4. window is ready → add the max
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
