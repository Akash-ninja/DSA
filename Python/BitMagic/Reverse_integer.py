import math


class Solution:
    def reverse(self, x: int) -> int:
        """
        Approach: using while loop and modulus operator
        note: checking 32-bit integer case is important here
        """
        # init
        INT_MIN = -pow(2, 31)
        INT_MAX = pow(2, 31) - 1

        sign = 1 if x > 0 else -1
        reversed_num = 0

        # edge cases:
        if x <= INT_MIN:
            return 0

        num = abs(x)

        # reverse logic
        while num > 0:
            digit = num % 10
            if reversed_num <= INT_MAX / 10:
                reversed_num = reversed_num * 10 + digit
                num = math.floor(num / 10)
            else:
                return 0

        return reversed_num * sign
