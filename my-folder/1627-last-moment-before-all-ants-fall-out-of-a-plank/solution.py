class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # initialize a variable to keep track of th emaximum time 
        time = 0

        # iterate through the positions of ants moving to the left
        for pos in left:
            # update the maximum time if the current left-moving ant's position is greater than the previously recorded maximum time
            time = max(time, pos)

        # iterate through the positions of ants moving to the right
        for pos in right:

            #Update the maximum time if the current right-moving ant's position is greater than the previously recorded maximum time
            time = max(time, n-pos)

            # The final 'time' variable contains the maximum time, which is when the last ant(s) fall off the plank, so return it as the result
        return time
