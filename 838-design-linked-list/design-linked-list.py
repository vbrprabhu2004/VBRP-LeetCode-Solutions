# Doubly Linked List
class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - index - 1):
                curr = curr.prev
        return curr.val

    def addAtHead(self, val):
        self._addNodeAfter(self.head, Node(val))

    def addAtTail(self, val):
        self._addNodeAfter(self.tail.prev, Node(val))

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
        else:
            node = self._getNode(index)
            self._addNodeAfter(node.prev, Node(val))

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        node = self._getNode(index)
        self._deleteNode(node)
    
    def _addNodeAfter(self, prev, node):
        nxt = prev.next
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node
        self.size += 1
    
    def _deleteNode(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1

    def _getNode(self, index):
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - index - 1):
                curr = curr.prev
        return curr
