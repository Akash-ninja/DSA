import math


class Solution:
    def isDistancePossible(self, position, m, distance):
        """
        Returns whether all balls can be placed or not in the given distance
        """
        balls_placed = 1
        last_ball_placed = position[0]

        i = 1
        while balls_placed < m and i < len(position):
            # from |x-y|, it checks y >= x + distance and, places the ball
            # where x = last ball position
            if position[i] >= last_ball_placed + distance:
                balls_placed += 1
                last_ball_placed = position[i]

            i += 1

        return balls_placed == m

    def maxDistance(self, position: List[int], m: int) -> int:
        """
        Returns maximum for the minimum magnetic force
        Solution approach: maximising the distance using Binary search after sorting the array
        """
        position.sort()

        start = 1
        end = position[-1]
        ans = 1

        while start <= end:
            mid = math.floor((start + end) / 2)

            if self.isDistancePossible(position, m, mid):
                # shorten the search space in right part of the mid to maximise the distance
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans
