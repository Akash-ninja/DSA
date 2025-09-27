# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invert(self, node):
        if node:
            left = self.invert(node.left)  # stores left node ref
            right = self.invert(node.right)
            node.left = right  # interchanging links
            node.right = left
        return node

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Approach: Invert left subtree and right subtree via taking reference and interchanging it
        """
        return self.invert(root)
