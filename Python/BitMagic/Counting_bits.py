class Solution:
    def count_set_bits(self, num):
        count = 0

        # assuming it a 32-bit integer
        for i in range(0, 31):
            # logic: checks each number set bit's
            if num & (1 << i) > 0:
                count += 1

        return count

    def countBits(self, n: int) -> List[int]:
        """
        Approach: using bitwise operators (<< and &)
        """
        ans = []

        for i in range(0, n + 1):
            ans.append(self.count_set_bits(i))

        return ans
