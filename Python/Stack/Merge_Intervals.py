class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Solution approach:
            1. Sort the intervals
            2. compare current interval (lowest) with last one (highest) with the help of stack
            3. Push in both cases
               Pop from the stack only when the interval comparison is true
        """
        intervals.sort()

        answer = [intervals[0]]  # treated as stack

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_interval = answer[-1]

            # point '2': Merging intervals here
            if current_interval[0] <= last_interval[1]:
                new_interval = [
                    min(last_interval[0], current_interval[0]),
                    max(last_interval[1], current_interval[1]),
                ]
                answer.pop(-1)
                answer.append(new_interval)

            else:
                answer.append(current_interval)

        return answer
