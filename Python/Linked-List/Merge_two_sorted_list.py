# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addToList(self, head, tail, node_to_add):
        new_node = ListNode(node_to_add.val)

        # when output list is empty
        if not head:
            head = new_node
            tail = new_node
        else:
            # move the tail pointer to point the node
            tail.next = new_node
            tail = new_node

        # return head, tail  # returns as a tuple
        return {"head": head, "tail": tail}

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        first = list1
        second = list2

        # for output list
        head = tail = None

        # iteration: when anyone of the list has nodes
        while first or second:
            node_to_copy = None

            # when both list are present
            if first and second:
                if first.val < second.val:
                    node_to_copy = first
                    first = first.next
                else:
                    node_to_copy = second
                    second = second.next
            elif first:
                node_to_copy = first
                first = first.next
            else:
                node_to_copy = second
                second = second.next

            # add the required node to the output list
            obj = self.addToList(head, tail, node_to_copy)
            head = obj.get("head")
            tail = obj.get("tail")

        return head  # head of the merged linked list
