class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        # Last element of postorder is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # Find the index of the root in inorder
        index = inorder.index(root_val)

        # Important: build right subtree before left since we pop from the end
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)

        return root
