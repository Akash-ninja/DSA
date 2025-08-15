# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution:
    def countNodes(self, pointer):
        count = 0
        while pointer:
            count += 1
            pointer = pointer.next

        return count

    def findNodeAtPosition(self, pointer, count):
        while count > 0:
            if pointer:
                pointer = pointer.next

            count -= 1

        return pointer

    def reverse(self, pointer, tail1):
        """
        Reversed list using iteration - because recursion internally uses stack which could forfeit constraint of O(1) space complexity
        """
        temp_pointer = pointer  # to avoid reversing the original list
        prev_prev_pointer = prev_pointer = None

        # reversing list through sliding pointers
        while temp_pointer:
            prev_prev_pointer = prev_pointer
            prev_pointer = temp_pointer
            temp_pointer = temp_pointer.next

            prev_pointer.next = prev_prev_pointer  # prev_pointer will become head node for reversed list

        tail1.next = prev_pointer  # links the tail end of 1st half to the 2nd half

        return {"tail1": tail1}

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Algo reverses the list from the middle and compares the values - O(1) space complexity
        """
        size = self.countNodes(head)
        if size == 1:
            return True

        # For odd size list, mid = mid + 1
        mid_of_list = math.floor(size / 2)
        if size % 2 != 0:
            mid_of_list += 1

        # locates head node from mid
        head2 = self.findNodeAtPosition(head, mid_of_list)
        tail1 = self.findNodeAtPosition(
            head, mid_of_list - 1
        )  # Need tail end of 1st half of the linked list to join 2nd half

        # reversing the list from the middle
        obj = self.reverse(head2, tail1)
        tail1 = obj.get("tail1")

        # traverse and compares the values from 1st half to 2nd half of the list
        first = head
        second = tail1.next
        while first and second:
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True
