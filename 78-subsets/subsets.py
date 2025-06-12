class Solution(object):
    def subsets(self, nums):
        res = [[]]  # Start with the empty subset
        
        for num in nums:
            new_subsets = []
            for item in res:
                new_item = item + [num]  # Create a new subset including current num
                new_subsets.append(new_item)
            res.extend(new_subsets)  # Add all new subsets to the result
        
        return res
