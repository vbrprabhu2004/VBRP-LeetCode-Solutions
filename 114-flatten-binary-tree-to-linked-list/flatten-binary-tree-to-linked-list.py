# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None  # global pointer to previous node

        def dfs(node):
            if not node:
                return
            
            # Traverse right first, then left (because we reverse connect)
            dfs(node.right)
            dfs(node.left)
            
            # Modify pointers to flatten
            node.right = self.prev
            node.left = None
            self.prev = node  # move prev to current

        dfs(root)
