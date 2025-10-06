# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Approach: point out observation that one of the node among p,q will be on left side and one of the node among p,q will be on right side
        """
        if not root:
            return None

        if root.val > p.val and root.val > q.val:
            # search in left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            # search in right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
