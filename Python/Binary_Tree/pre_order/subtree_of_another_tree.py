# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, tree1_node, tree2_node):
        if not tree1_node and not tree2_node:
            return True
        if not tree1_node or not tree2_node:
            return False
        if tree1_node.val != tree2_node.val:
            return False

        return self.isSameTree(tree1_node.left, tree2_node.left) and self.isSameTree(
            tree1_node.right, tree2_node.right
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Approach: another 'subRoot' tree should be same as subtree of the first one if it is contained within it so,
        applied same tree logic and recursively checked subtree
        """
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
