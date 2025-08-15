# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reversing Iteratively: using sliding pointers
        """
        prev_prev_head = prev_head = None
        tail = head

        while tail:
            # sliding 3 pointers
            prev_prev_head = prev_head
            prev_head = tail
            tail = tail.next

            # reversing links
            prev_head.next = prev_prev_head

        head = prev_head  # assigned last node to head
        return head


class Solution2:
    def __init__(self, first=None):
        self.first = first

    # two pointers q and p keeps tracks of links
    def reverse(self, q, p):
        if p:
            self.reverse(p, p.next)
            p.next = q
        else:
            self.first = q

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.reverse(None, head)
        return self.first
