class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

        if len(self.min_arr) != 0:
            if self.min_arr[-1][0] > val:
                self.min_arr.append([val, 1])
            elif self.min_arr[-1][0] == val:
                self.min_arr[-1][1] += 1
        else:
            self.min_arr.append([val, 1])

    def pop(self) -> None:
        tmp = self.arr.pop()

        if (len(self.min_arr)) != 0 and self.min_arr[-1][0] == tmp:
            if self.min_arr[-1][1] > 1:
                self.min_arr[-1][1] -= 1
            else:
                self.min_arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_arr[-1][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()