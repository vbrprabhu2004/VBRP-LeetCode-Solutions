class BSTIterator(object):

    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        # Push all left nodes to stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        # Pop the top element
        node = self.stack.pop()
        # Push left path of right subtree
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0


