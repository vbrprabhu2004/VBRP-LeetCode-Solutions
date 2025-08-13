import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)  # turn list into a min-heap
        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        # If heap grows beyond size k, remove the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # Smallest in heap = k-th largest in stream
        return self.heap[0]
