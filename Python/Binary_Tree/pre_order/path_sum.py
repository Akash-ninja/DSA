# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.answer = False

    def pre_order(self, node, parent_sum, target_sum):
        if node:
            sum_till_me = parent_sum + node.val

            if not node.left and not node.right and sum_till_me == target_sum:
                self.answer = True

            if node.left:
                self.pre_order(node.left, sum_till_me, target_sum)
            if node.right:
                self.pre_order(node.right, sum_till_me, target_sum)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        Approach: Similar to path sum 2
        """
        self.pre_order(root, 0, targetSum)
        return self.answer
