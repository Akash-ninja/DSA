class Solution:
    def isValid(self, s: str) -> bool:
        """
        Solution using stack push and pop methods of list
        """
        st = []

        for i, ch in enumerate(s):
            # for opening brackets
            if ch == "(" or ch == "{" or ch == "[":
                st.append(ch)

            else:
                if len(st) == 0:
                    return False
                else:
                    lch = st[-1]
                    # for closing brackets
                    if (
                        (lch == "(" and ch == ")")
                        or (lch == "{" and ch == "}")
                        or (lch == "[" and ch == "]")
                    ):
                        st.pop(len(st) - 1)
                    else:
                        return False

        # if after push and pop stack becomes empty then all brackets pair has been found
        if len(st) == 0:
            return True

        return False
