class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = [dist[i] / speed[i] for i in range(len(dist))]

        arrival_time.sort()

        for i in range(len(arrival_time)):
            if arrival_time[i] <= i:
                return i

        return len(dist)

