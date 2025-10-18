class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root):
        def subtreeHeights(root1):
            if root1 is None:
                return True  # An empty tree is balanced

            diff = abs(self.maxDepth(root1.left) - self.maxDepth(root1.right))

            if diff > 1:
                return False
            else:
                return subtreeHeights(root1.left) and subtreeHeights(root1.right)

        return subtreeHeights(root)