class MyQueue(object):

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        self._transfer()
        return self.stack_out.pop()

    def peek(self):
        self._transfer()
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out

    def _transfer(self):
        # Transfer only when stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
