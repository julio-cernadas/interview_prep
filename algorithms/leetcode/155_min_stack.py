class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
            return

        stack_val, min_val = self.stack[-1]
        if val < min_val:
            min_val = val

        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        stack_val, min_val = self.stack[-1]
        return stack_val

    def get_min(self) -> int:
        stack_val, min_val = self.stack[-1]
        return min_val


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.get_min())
obj.pop()
print(obj.top())
print(obj.get_min())
