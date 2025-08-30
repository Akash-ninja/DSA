import math


class Solution:
    def isEatingPossible(self, piles: list, h, hours):
        """
        Tells whether input 'hours' is enough for eating all the bananas present in the piles
        """
        eat_hrs_taken_by_koko = 0

        for no_of_bananas in piles:
            eat_hrs_taken_by_koko += math.ceil(no_of_bananas / hours)

        return eat_hrs_taken_by_koko <= h

    def minEatingSpeed(self, piles: list, h: int) -> int:
        """
        Solution approach: using binary search to find out min. eating hours before guards return
        """
        start = 1
        end = max(piles)
        ans = end

        while start <= end:
            mid = math.floor((start + end) / 2)

            if self.isEatingPossible(piles, h, mid):
                # shorten the search space to find minimum of minimum
                # thats why search in left space
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans
