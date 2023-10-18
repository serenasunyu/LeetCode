class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        #  Create a graph to represent the prerequisites using an adjacency list.
        graph = [[] for _ in range(n)]

        for prev, next in relations:
            graph[prev - 1].append(next - 1)
        
        # Create a memoization table (an array) to store the minimum time needed to complete each course.
        memo = [-1] * n

        # Define a recursive function to calculate the minimum time to complete a course.
        def calculateTime(course):
            if memo[course] != -1:
                return memo[course]
            
            if not graph[course]:
                memo[course] = time[course]
                return memo[course]

            max_prerequisite_time = 0
            for prereq in graph[course]:
                max_prerequisite_time = max(max_prerequisite_time, calculateTime(prereq))
            
            memo[course] = max_prerequisite_time + time[course]
            return memo[course]

        # Initialize a variable to keep track of the overall minimum time.
        overall_min_time = 0
        for course in range(n):
            overall_min_time = max(overall_min_time, calculateTime(course))
        
        return overall_min_time
