class Solution(object):
    def flatten(self, root):
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
