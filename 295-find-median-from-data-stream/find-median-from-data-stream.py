import heapq

class MedianFinder(object):

    def __init__(self):
        # max_heap for lower half (store as negative for max behavior)
        self.max_heap = []
        # min_heap for upper half
        self.min_heap = []

    def addNum(self, num):
        # Add to max_heap (as negative value for max-heap behavior)
        heapq.heappush(self.max_heap, -num)

        # Ensure all elements in max_heap are <= elements in min_heap
        if self.max_heap and self.min_heap and (-self.max_heap[0]) > self.min_heap[0]:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)

        # Balance heaps size difference
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0

