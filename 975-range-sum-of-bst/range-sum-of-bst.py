class Solution(object):
    def rangeSumBST(self, root, low, high):
        self.sum1 = 0
        def inorder(self, root):
            if not root:
                return
            inorder(self, root.left)
            #res.append(root.val)
            if(root.val <= high and low <= root.val):
                self.sum1 += root.val
            # 1 3 5 6 7 10 13 15 18
            # low = 6 high = 10
            inorder(self, root.right)
        inorder(self, root)
        return self.sum1