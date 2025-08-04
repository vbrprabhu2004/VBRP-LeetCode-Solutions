class Codec(object):
    def serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        tokens = data.split(',')
        self.index = 0

        def build():
            if tokens[self.index] == '#':
                self.index += 1
                return None
            node = TreeNode(int(tokens[self.index]))
            self.index += 1
            node.left = build()
            node.right = build()
            return node
        
        return build()
