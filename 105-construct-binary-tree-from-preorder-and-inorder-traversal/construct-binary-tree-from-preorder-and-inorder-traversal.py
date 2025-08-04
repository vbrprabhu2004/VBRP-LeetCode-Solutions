class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        # First element of preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # Find the index of the root in inorder
        index = inorder.index(root_val)

        # Recursively build left and right subtrees
        root.left = self.buildTree(preorder[1:1+index], inorder[:index])
        root.right = self.buildTree(preorder[1+index:], inorder[index+1:])

        return root
