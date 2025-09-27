# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    sum = 0

    def pre_order(self, node, isLeft):
        if node:
            isLeaf = True

            if node.left:
                self.pre_order(node.left, True)
                isLeaf = False

            if node.right:
                self.pre_order(node.right, False)
                isLeaf = False

            if isLeaf and isLeft:
                self.sum += node.val

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Approach: every time, we'll call the node and pass isLeft value down the node.
        Therefore, only when the node is left and leaf, we calculate the sum
        """
        self.pre_order(root, False)
        return self.sum
