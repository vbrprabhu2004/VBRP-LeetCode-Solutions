class Solution(object):
    def rangeSumBST(self, root, low, high):
        sum1 = 0
        res = []
        def inorder(self, root):
            if not root:
                return
            inorder(self, root.left)
            res.append(root.val)
            # 1 3 5 6 7 10 13 15 18
            # low = 6 high = 10
            inorder(self, root.right)
        inorder(self, root)
    
        for i in res:
            if(i <= high and low <= i):
                sum1 += i
        return sum1