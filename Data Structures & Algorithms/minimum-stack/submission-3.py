class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.Min:
            self.Min = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.Min:
            if self.stack:
                self.Min = min(self.stack)
            else:
                self.Min = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.Min
        
