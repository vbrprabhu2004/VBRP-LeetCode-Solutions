from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq = sorted(freq.items(), key = lambda x : x[1], reverse = True)
        result = []
        for num, count in sorted_freq[:k]:
            result.append(num)
        return result