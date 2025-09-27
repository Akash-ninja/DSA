# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    # post order traversal
    def traverse_and_check(self, f1, f2):
        if not f1 and not f2:
            return True  # if in both side of subtree node not present
        if not f1 or not f2:
            return False  # else, if only node is present

        is_same = f1.val == f2.val
        is_Sym1 = self.traverse_and_check(f1.left, f2.right)
        is_Sym2 = self.traverse_and_check(f1.right, f2.left)

        return is_same and is_Sym1 and is_Sym2

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Problem: To compare the mirror version of a subtrees rooted at node

        Approach: While traversing,
        1) compares similar node values
        2) it checks symmetricity for - left node of left subtree to the right node of right subtree and vice-versa
        """
        return self.traverse_and_check(root.left, root.right)
