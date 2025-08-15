class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input array is sorted
        n = len(numbers)
        left_pointer = 0
        right_pointer = n - 1

        output = []
        # loop:
        while left_pointer < right_pointer:
            sum = numbers[left_pointer] + numbers[right_pointer]

            if sum < target:
                left_pointer += 1
            elif sum > target:
                right_pointer -= 1
            else:
                output.append(left_pointer + 1)
                output.append(right_pointer + 1)
                break

        return output
