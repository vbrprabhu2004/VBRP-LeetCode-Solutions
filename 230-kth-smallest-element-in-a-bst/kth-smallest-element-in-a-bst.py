class Solution(object):
    def kthSmallest(self, root, k):
       
        self.count = 0         # Counter to track the number of nodes visited
        self.result = None     # Variable to store the k-th smallest value

        def inorder(node):
            # Stop traversal if node is None or result is already found
            if not node or self.result is not None:
                return

            # Traverse the left subtree
            inorder(node.left)

            # Visit the current node
            self.count += 1
            if self.count == k:
                self.result = node.val
                return

            # Traverse the right subtree
            inorder(node.right)

        inorder(root)
        return self.result
