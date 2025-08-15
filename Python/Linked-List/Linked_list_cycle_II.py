# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Solution using Floyd Tortoise and Hare algorithm -
        Steps -
        1. Detects the cycle
            - detection done using infinite loop
            - if there is no loop, then fast.next becomes null and returns null
            - algo says there are two pointers slow and fast => slow moves 1 step and fast moves 2 steps at a time
            - stores meeting point where slow and fast will meet and breaks out of the loop

        2. Finds out the starting point of the loop/cycle
            - initializes a start pointer
            - runs loop wherein this start and meeting pointer moves by 1
            - algo says if the cycle is detected then definitely these two pointers will meet and that will be starting point
        """

        slow = fast = head
        meet_point = None

        # infinite loop
        while True:
            # no cycle: returns null
            if not fast or not fast.next:
                return None

            # moves slow and fast pointers
            slow = slow.next
            fast = fast.next.next

            # cycle detected
            if slow == fast:
                meet_point = fast
                break

        # finds the starting point of the cycle
        start = head
        while start != meet_point:
            start = start.next
            meet_point = meet_point.next

        return start
