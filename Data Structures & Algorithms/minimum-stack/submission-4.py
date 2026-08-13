class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimum or val < self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.getMin() and self.minimum and popped not in self.stack:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1] if self.minimum else 0
