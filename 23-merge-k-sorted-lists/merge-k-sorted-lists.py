import heapq
class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        counter = 0  # to avoid comparison of ListNode when values are equal

        # Step 1: Push first node of each list into heap
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode(0)
        current = dummy

        # Step 2: Pop smallest element and push its next node
        while heap:
            val, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next
