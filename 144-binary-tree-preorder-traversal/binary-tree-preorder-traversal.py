class Solution:
    def preorderTraversal(self, root):
        res = []

        def preorder(node):
            if node is None:
                return
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return res
