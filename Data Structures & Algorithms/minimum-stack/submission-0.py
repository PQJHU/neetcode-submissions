class MinStack:

    def __init__(self):
        self.stack = []
        self.min_pos_stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.min_pos_stack.append(0)
        else:
            if val <= self.stack[self.min_pos_stack[-1]]:
                self.min_pos_stack.append(len(self.stack))  # record the actual index -1 = len(stack)
            else:
                self.min_pos_stack.append(self.min_pos_stack[-1])  # repeat the last pos

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_pos_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_pos_stack[-1]]
