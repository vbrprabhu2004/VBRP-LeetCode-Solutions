class Solution(object):
    def findKthPositive(self, arr, k):
        new_list = list(range(1, 10000))  

        missing = []

        for num in new_list:
            if num not in arr:
                missing.append(num)
        
        return missing[k - 1]
