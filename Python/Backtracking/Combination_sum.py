import math


class Solution:
    def __init__(self):
        self.answer = []

    def func(self, i, remaining, combination, candidates):
        """
        Main backtracking call and logic sits here.
        1. we select each element then
            - find out max no. of times it can be taken
            - calculate remaining target
            - and then try out each combination for that selected element
        """
        n = len(candidates)
        if i == n:
            if remaining == 0:
                temp = []
                for el in combination:
                    temp.append(el)
                self.answer.append(temp)

        else:
            current_element = candidates[i]
            max_times = math.floor(remaining / current_element)

            for k in range(0, max_times + 1):
                new_target = remaining - (k * current_element)

                for j in range(0, k):
                    combination.append(current_element)

                # recursive call
                self.func(i + 1, new_target, combination, candidates)

                for x in range(0, k):
                    combination.pop(-1)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: using backtracking exploring all possibilities
        """

        self.func(0, target, [], candidates)

        return self.answer
