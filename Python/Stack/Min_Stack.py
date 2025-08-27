class MinStack:
    """
    Solution using another stack for tracking min. element
    """

    def __init__(self):
        self.a = list()
        self.b = list()

    def push(self, val: int) -> None:
        self.a.append(val)

        # push in stack 'b' only when the incoming value is less than the stack top of b
        size_b = len(self.b)
        if size_b == 0 or self.b[-1] >= val:
            self.b.append(val)

    def pop(self) -> None:

        # pops from both stack only when both stack top has equal value
        if self.a[-1] == self.b[-1]:
            self.a.pop(-1)
            self.b.pop(-1)
        else:
            self.a.pop(-1)

    def top(self) -> int:
        return self.a[-1]

    def getMin(self) -> int:
        return self.b[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
