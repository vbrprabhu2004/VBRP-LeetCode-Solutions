class Solution(object):
    def findSecondMinimumValue(self, root):
        values = set()

        def dfs(node):
            if node:
                values.add(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        values = list(values)
        if len(values) < 2:
            return -1
        values.remove(min(values))  # remove smallest
        return min(values)          # now the smallest = second minimum
