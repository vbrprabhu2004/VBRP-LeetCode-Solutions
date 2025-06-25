class Solution:
    def postorderTraversal(self, root):
        res = []

        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        postorder(root)
        return res
