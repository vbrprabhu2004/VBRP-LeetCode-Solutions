class Solution(object):
    def sortList(self, head):
        # Base case: if the list is empty or has only one element
        if not head or not head.next:
            return head

        # Step 1: Split the list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None  # break the list

        # Step 2: Sort each half
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge the sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next
