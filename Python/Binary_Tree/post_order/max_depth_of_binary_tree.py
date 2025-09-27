# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def traverse(self, node):
        if not node:
            return 0
        else:
            left_depth = self.traverse(node.left)
            right_depth = self.traverse(node.right)
            return max(left_depth, right_depth) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Approach: Max. of left subtree and right subtree + 1
        """
        return self.traverse(root)
