class Solution(object):
    def insert(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def bstFromPreorder(self, preorder):
        root = None
        for val in preorder:
            root = self.insert(root, val)
        return root
