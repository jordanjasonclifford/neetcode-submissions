class MinStack:

    def __init__(self):
        # main stack stores all values
        self.stack = []

        # minStack stores the minimum value at each position
        self.minStack = []

    def push(self, val: int) -> None:
        # push value onto main stack
        self.stack.append(val)

        # compute new minimum:
        # compare current value with previous minimum (top of minStack)
        # if minStack is empty, just use val
        val = min(val, self.minStack[-1] if self.minStack else val)

        # push the current minimum onto minStack
        self.minStack.append(val)
        

    def pop(self) -> None:
        # pop from both stacks to keep them in sync
        self.stack.pop()
        self.minStack.pop()


    def top(self) -> int:
        # return the top of the main stack
        return self.stack[-1] 


    def getMin(self) -> int:
        # return the current minimum (top of minStack)
        return self.minStack[-1]