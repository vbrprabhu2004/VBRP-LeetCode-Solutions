class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        
        # Step 2: Sort items in the dictionary by frequency in descending order
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # sorted_items = [(1, 3), (2, 2), (3, 1)]

        # Step 3: Extract top k elements based on frequency
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        # When i = 0 → result = [1]
        # When i = 1 → result = [1, 2]

        return result
