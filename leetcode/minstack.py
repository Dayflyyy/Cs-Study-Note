class MinStack(object):
    min = 0;
    st = []

    def __init__(self):
        self.st = []
        self.min

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if (len(self.st) == 0):
            self.min = val
        self.st.append(val)
        if (val < self.min):
            self.min = val

    def pop(self):
        """
        :rtype: None
        """
        if (len(self.st) > 0):
            item = self.st.pop()
            if (item == self.min):
                self._find_min()
            return item

    def top(self):
        """
        :rtype: int
        """
        if (len(self.st) > 0):
            return self.st[len(self.st) - 1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

    def _find_min(self):
        if (len(self.st) == 0):
            self.min = float("inf")
            return
        _min = self.st[0]
        for i in self.st:
            if i < _min:
                _min = i
        self.min = _min

test=MinStack()
test.push(-2)
test.push(0)
test.push(-3)
print(test.getMin())
print(test.pop())
print(test.top())
print(test.getMin())



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
