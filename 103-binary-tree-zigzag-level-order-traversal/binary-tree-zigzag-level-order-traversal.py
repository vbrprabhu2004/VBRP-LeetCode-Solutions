from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

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

            # Reverse the level if it's right to left
            if not left_to_right:
                level_nodes.reverse()

            result.append(level_nodes)
            left_to_right = not left_to_right  # Flip direction

        return result  