class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def depth(root):
            if not root:
                return 0
            left_gain = max(depth(root.left), 0)
            right_gain = max(depth(root.right), 0)

            consecutive_sum = root.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, consecutive_sum)
            return root.val + max(left_gain, right_gain)
        depth(root)
        return self.max_sum
            
