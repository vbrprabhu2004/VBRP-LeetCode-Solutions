from collections import deque

class Solution(object):
    def levelOrder(self, root):
        res = []
        if root is None:
            return res

        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []  

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(level_nodes)  

        return res
