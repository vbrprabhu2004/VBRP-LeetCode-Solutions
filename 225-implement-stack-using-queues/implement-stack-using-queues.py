from collections import deque
class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)
        # Rotate the queue to bring the new element to the front
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
            
    def pop(self):
        return self.queue.popleft()        

    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0
