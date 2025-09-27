# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def root_height(self, node):
        if not node:
            return 0
        else:
            left_height = self.root_height(node.left)
            right_height = self.root_height(node.right)

            if (
                left_height == -1
                or right_height == -1
                or abs(left_height - right_height) > 1
            ):
                return -1
            else:
                return max(left_height, right_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Approach: finds height of node while doing post order traversal
        """
        ans = self.root_height(root)
        if ans == -1:
            return False

        return True
