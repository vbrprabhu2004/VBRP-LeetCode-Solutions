class Solution:
    def inorderTraversal(self, root):
        res = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res
