class Solution(object):
    def rangeSumBST(self, root, low, high):
        self.sum1 = 0
        def inorder(self, root):
            if not root:
                return
            inorder(self, root.left)
            #res.append(root.val)
            inorder(self, root.right)
            if(root.val <= high and low <= root.val):
                self.sum1 += root.val
        inorder(self, root)
        return self.sum1