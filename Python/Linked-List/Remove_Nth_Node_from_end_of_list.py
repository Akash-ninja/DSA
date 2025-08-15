# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Uses two pointer method, slow and fast pointers
        """
        slow = fast = head

        # fast traverses 'n' times
        for i in range(n):
            fast = fast.next

        # if the list contains only 1 node
        if not fast:
            return slow.next

        # until fast next node is null
        while fast.next:
            slow = slow.next
            fast = fast.next

        # connecting links
        slow.next = slow.next.next
        return head
