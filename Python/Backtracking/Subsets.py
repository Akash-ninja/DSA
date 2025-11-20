class Solution:
    def __init__(self):
        self.powerset = []
        self.original = []

    def backtrack(self, i, subset):
        """
        a. Does the main backtracking, first selects excluding case then selects including element case
        b. Once, the recursion reaches its termination point, then collects all elements in a temp. list
        then fills the powerset
        c. confusing code (removal of last el from subset) - subset.pop(-1)
            This is to avoid any side-affects
            and, Since it backtracks recusrively so on returning phase,
            it has to reach its original point where it has taken the decision thats why popping
        """
        n = len(self.original)
        if i >= n:
            temp = []
            for i in range(0, len(subset)):
                temp.append(subset[i])

            self.powerset.append(temp)
        else:
            # exclude
            self.backtrack(i + 1, subset)

            # include
            subset.append(self.original[i])
            self.backtrack(i + 1, subset)
            subset.pop(-1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: explore all possibilites using backtracking method
        """
        # init
        self.original = nums
        subset = []

        # invoke backtracking
        self.backtrack(0, subset)

        return self.powerset
