class SeatManager:

    def __init__(self, n: int):
        self.last = 0
        self.pq = []

    def reserve(self) -> int:
        # If the min-heap is empty, simply increment the last counter and return it.
        if not self.pq:
            self.last += 1
            return self.last
        # If the min-heap has seats (i.e., there are unreserved seats), pop the smallest seat from the heap and return it.
        return heapq.heappop(self.pq)

    def unreserve(self, seatNumber: int) -> None:
        # If the seat being unreserved is the last seat in the continuous sequence, decrement the last counter.
        if seatNumber == self.last:
            self.last -= 1
        # Otherwise, add the unreserved seat to the min-heap.
        else:
            heapq.heappush(self.pq, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
