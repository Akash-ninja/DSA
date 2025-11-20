class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        Approach: using leftshift operator
        """
        # 1. init
        a = dividend
        b = divisor

        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        sign = 1
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            sign = -1

        # 2. edge case
        if a == INT_MIN and b == -1:
            return int(INT_MAX)
        elif a == INT_MIN and b == 1:
            return int(INT_MIN)
        elif a == INT_MAX and b == 1:
            return int(INT_MAX)

        a = abs(a)
        b = abs(b)

        # edge case
        if a == b:
            return 1 * sign

        quotient = 0

        # 3. divison logic
        while a >= b:
            i = 0
            # main logic loop
            while (b << i) <= a:
                i += 1

            i -= 1
            quotient += pow(2, i)
            a = a - (b << i)

        return quotient * sign
