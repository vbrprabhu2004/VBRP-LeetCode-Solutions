class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))