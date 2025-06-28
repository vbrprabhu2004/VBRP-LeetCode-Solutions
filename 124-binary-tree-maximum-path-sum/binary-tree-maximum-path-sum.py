class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def helper(node):
            if node is None:
                return 0
            
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right),0)

            current_path_sum = node.val + left_gain + right_gain

            self.max_sum = max(self.max_sum, current_path_sum)

            return node.val + max(left_gain, right_gain)
        
        helper(root)
        return self.max_sum