# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.first_parent = None
        self.first_level = -1
        self.second_parent = None
        self.second_level = -1

    # pre-order traversal
    def traverse(self, node, x, y, parent, level):
        if node:
            # stores the parent and level of node x
            if node.val == x:
                self.first_parent = parent
                self.first_level = level

            if node.val == y:
                self.second_parent = parent
                self.second_level = level

            if node.left:
                self.traverse(node.left, x, y, node, level + 1)
            if node.right:
                self.traverse(node.right, x, y, node, level + 1)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        Approach: passing parent node and level while doing traversal and stores the parent and level of x and y
        and atfer completion of traversal, checks for different parent and same level of x and y nodes
        """
        self.traverse(root, x, y, None, 1)
        return (
            self.first_parent != self.second_parent
            and self.first_level == self.second_level
        )
