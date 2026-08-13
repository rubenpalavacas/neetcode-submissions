class MinStack:
    """
    Added improvements from NeetCode's solution:
    - Always add the current minimum element to the minstack. That way, when you pop,
    you pop in both stacks and you always have the minimum value for that given state
    of the stack. 
    - With that, you also remove the "if self.minimum" check in the getMin() function
    """

    def __init__(self):
        self.stack = []
        self.minimum = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        minimum = min(val, self.minimum[-1] if self.minimum else val)
        self.minimum.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
