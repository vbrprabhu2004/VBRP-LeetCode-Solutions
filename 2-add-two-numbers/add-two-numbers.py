class Solution:
    def addTwoNumbers(self, l1, l2):
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        a = l1.val + l2.val
        p = ListNode(a % 10)
        p.next = self.addTwoNumbers(l1.next, l2.next)
        if a >= 10:
            p.next = self.addTwoNumbers(p.next, ListNode(1))
        return p