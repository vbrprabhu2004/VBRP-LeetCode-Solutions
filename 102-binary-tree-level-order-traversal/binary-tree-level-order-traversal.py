class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []       
        result = [] 
        queue = [root]

        while queue:
            level = []
            next_level = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(level)
            queue = next_level
        return result
