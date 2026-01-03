class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []        

    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val == self.minStack[-1]:
                self.minStack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.minStack[-1] if self.minStack else None