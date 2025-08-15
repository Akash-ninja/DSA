# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        # Detection using Floyd Tortoise and Hare algorithm
        slow = head
        fast = head.next.next

        while slow and fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
