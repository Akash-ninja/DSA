# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    good_nodes_count = 0

    def traverse(self, node, max_till_parent):
        if node:
            if max_till_parent is None or node.val >= max_till_parent:
                self.good_nodes_count += 1

            max_till_me = (
                max(max_till_parent, node.val)
                if max_till_parent is not None
                else node.val
            )

            self.traverse(node.left, max_till_me)
            self.traverse(node.right, max_till_me)

    def goodNodes(self, root: TreeNode) -> int:
        """
        Approach: every node passes max_value down to child node and so,
        it count "good nodes" only when the node value is greater than or equal to the max value it got from parent
        """
        self.traverse(root, None)
        return self.good_nodes_count
