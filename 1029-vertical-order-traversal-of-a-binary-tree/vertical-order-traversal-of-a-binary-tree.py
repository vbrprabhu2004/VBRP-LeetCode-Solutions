import collections
import heapq

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        # Dictionary: col index -> list of (row, val)
        node_map = collections.defaultdict(list)
        queue = [(0, 0, root)]  # (col, row, node)

        while queue:
            col, row, node = queue.pop(0)
            heapq.heappush(node_map[col], (row, node.val))

            if node.left:
                queue.append((col - 1, row + 1, node))
                queue[-1] = (col - 1, row + 1, node.left)
            if node.right:
                queue.append((col + 1, row + 1, node))
                queue[-1] = (col + 1, row + 1, node.right)

        result = []
        for col in sorted(node_map.keys()):
            col_nodes = []
            heap = node_map[col]
            heap.sort()  # sort by row first, then val
            for row, val in heap:
                col_nodes.append(val)
            result.append(col_nodes)

        return result
