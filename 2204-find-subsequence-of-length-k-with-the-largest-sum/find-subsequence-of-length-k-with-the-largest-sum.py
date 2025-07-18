class Solution(object):
    def maxSubsequence(self, nums, k):
        # Pair each number with its original index
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort by value descending, and pick top-k elements
        top_k = sorted(indexed_nums, key=lambda x: x[0], reverse=True)[:k]
        
        # Sort the top-k elements by their original index to preserve order
        top_k_sorted = sorted(top_k, key=lambda x: x[1])
        
        # Extract the values only
        result = [num for num, _ in top_k_sorted]
        
        return result
