class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        val = self.stack[-1]
        return val
        
    def getMin(self) -> int:
        min = float("inf")
        for s in self.stack:
            if s < min:
                min = s
        return min
        
