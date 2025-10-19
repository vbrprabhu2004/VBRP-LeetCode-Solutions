class Solution(object):
    def kthSmallest(self, root, k):
        self.count = 0
        #self.temp = root.val
        def inorder(self, root):
            if not root:
                return 0
            inorder(self, root.left)
            self.count += 1
            if (self.count == k):
                self.temp = root.val
            inorder(self, root.right)
        inorder(self, root)
        return self.temp
