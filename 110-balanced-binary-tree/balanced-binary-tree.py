class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1

    def isBalanced(self, root):
        def subtreeHeights(root1):
            if root1 is None:
                return True  # An empty tree is balanced

            left_height = self.maxDepth(root1.left)
            right_height = self.maxDepth(root1.right)

            diff = abs(left_height - right_height)

            if diff > 1:
                return False
            else:
                return subtreeHeights(root1.left) and subtreeHeights(root1.right)

        return subtreeHeights(root)
