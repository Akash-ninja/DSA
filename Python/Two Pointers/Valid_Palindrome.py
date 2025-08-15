import re


class Solution:
    def isAlphaNumeric(self, ch):
        rex = r"[A-Za-z0-9]"
        return re.match(rex, ch)

    def isPalindrome(self, s: str) -> bool:
        # checks for empty string
        if not s.strip():
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()

            # check: alphanumeric
            if not self.isAlphaNumeric(left_char):
                left += 1
            elif not self.isAlphaNumeric(right_char):
                right -= 1
            elif left_char != right_char:
                return False
            else:
                left += 1
                right -= 1

        return True
