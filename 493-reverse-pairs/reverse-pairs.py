class Solution:
    def reversePairs(self, nums: List[int]) -> int:     
        N = len(nums)
        tot = 0
        sorted_right_side = [nums[-1]*2]
        
        for j in range(N-2,-1,-1):
            n = nums[j]
            # count of numbers that are < 2 * n
            tot += bisect.bisect_left(sorted_right_side,n)
            bisect.insort(sorted_right_side, n*2)

        return tot