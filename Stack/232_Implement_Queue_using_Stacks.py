# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if self.stack1:
            self.stack2.extend(self.stack1)
            self.stack1.clear()
            self.stack1.append(x)
            self.stack1.extend(self.stack2)
            self.stack2.clear()

        else:
            self.stack1.append(x)

    def pop(self) -> int:
        if self.stack1:
            return self.stack1.pop()

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
