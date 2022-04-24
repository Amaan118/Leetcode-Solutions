# https://leetcode.com/problems/design-front-middle-back-queue/


class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = list()
        self.front = -1
        self.back = 0

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        mid = len(self.queue)//2
        self.queue.insert(mid, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        print(self.queue)
        if len(self.queue):
            return self.queue.pop(0)
        return -1

    def popMiddle(self) -> int:
        if len(self.queue):
            if len(self.queue) % 2:
                mid = len(self.queue)//2
            else:
                mid = len(self.queue)//2 - 1
            return self.queue.pop(mid)
        return -1

    def popBack(self) -> int:
        if len(self.queue):
            return self.queue.pop(-1)
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
