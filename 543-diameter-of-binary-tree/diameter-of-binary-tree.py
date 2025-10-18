class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            # update global max diameter
            self.max_diameter = max(self.max_diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.max_diameter
