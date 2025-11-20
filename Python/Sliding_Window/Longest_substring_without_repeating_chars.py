class Solution:
    def isValid(self, obj):
        valid = True
        for value in obj.values():
            if value > 1:
                valid = False

        return valid

    def delete_char(self, obj, ch):
        if ch in obj:
            obj[ch] -= 1

    def add_to_obj(self, obj, ch):
        if ch not in obj:
            obj[ch] = 1
        else:
            obj[ch] += 1

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Approach: using sliding window method of using fp and sp pointers
        """
        # init
        fp = sp = 0  # pointers
        obj = {}  # tracking characters obj
        n = len(s)
        ans = 0  # stores answer

        # 'sp' pointer will move till n
        while sp < n:
            # 1. Add character to object
            self.add_to_obj(obj, s[sp])

            # 2. Delete the leftmost char (from tracking) if found repeated in obj
            while fp < sp and not self.isValid(obj):
                self.delete_char(obj, s[fp])
                fp += 1

            # 3. set answer
            length = sp - fp + 1
            if length > ans:
                ans = length

            sp += 1

        return ans
