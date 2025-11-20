class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32 bits of 1
        MAX_INT = 0x7FFFFFFF  # 2147483647

        while b != 0:
            carry = (a & b) & MASK
            carry <<= 1
            a = (a ^ b) & MASK
            b = carry & MASK

        # if a is a negative 32-bit number, convert to Python's negative int
        return a if a <= MAX_INT else ~(a ^ MASK)
