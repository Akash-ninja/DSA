class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_source = "".join(sorted(s))
        sorted_target = "".join(sorted(t))

        return sorted_source == sorted_target


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        ht_source = dict()
        ht_target = dict()

        # source dict fill up with exact count of letters
        for i, el in enumerate(s):
            if el in ht_source:
                ht_source[el] += 1
            else:
                ht_source[el] = 1

        # target dict fill up with exact count of letters
        for i, el in enumerate(t):
            if el in ht_target:
                ht_target[el] += 1
            else:
                ht_target[el] = 1

        if ht_source == ht_target:
            return True

        return False
