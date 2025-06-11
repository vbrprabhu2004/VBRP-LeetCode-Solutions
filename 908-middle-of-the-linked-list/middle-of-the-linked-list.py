class Solution(object):
    def middleNode(self, head):
        slow = fast = head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow
'''
slow: moves one step at a time
fast: moves two steps at a time
head: points to the start of the linked list

It is a two-pointer technique (also called the "tortoise and hare" approach) 
'''