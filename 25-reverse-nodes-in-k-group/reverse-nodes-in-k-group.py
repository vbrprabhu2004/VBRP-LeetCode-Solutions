class Solution(object):
    def reverseKGroup(self, head, k):
        # Helper function to reverse nodes between start and end
        def reverse(start, end):
            prev = end
            curr = start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Step 1: Find kth node
            kth = group_prev
            for i in range(k):
                kth = kth.next
                if not kth:   # if fewer than k nodes left → stop
                    return dummy.next

            # Step 2: Define group boundaries
            group_next = kth.next
            start = group_prev.next

            # Step 3: Reverse the k nodes
            new_head = reverse(start, group_next)

            # Step 4: Connect reversed group back to list
            group_prev.next = new_head
            group_prev = start
