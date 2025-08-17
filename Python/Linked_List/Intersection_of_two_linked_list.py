# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def countNodes(self, p):
        count = 0
        while p:
            count += 1
            p = p.next
        return count

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        n = self.countNodes(headA)
        m = self.countNodes(headB)
        first = headA
        second = headB

        # whichever list is larger, move that pointer equal to |m-n| times
        if n < m:
            count = m - n
            while count > 0:
                second = second.next
                count -= 1
        else:
            count = n - m
            while count > 0:
                first = first.next
                count -= 1

        # checks every node
        while first:
            if first == second:
                return first

            first = first.next
            second = second.next

        return None
