class MedianFinder:
    """
    def __init__(self):
        self.list = []
        

    def addNum(self, num: int) -> None:
        self.list.append(num)
        self.list.sort()

    def findMedian(self) -> float:
        if len(self.list) % 2 != 0:
            return self.list[len(self.list) // 2]
        else:
            return (self.list[len(self.list) // 2] + self.list[len(self.list) // 2 - 1]) / 2
    """

    def __init__(self):
        self.A = []
        self.B = []

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))


    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
