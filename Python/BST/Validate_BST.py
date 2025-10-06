# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValid(self, node, lower, upper):
        print(f"isValid called with node={node} and lower={lower} and upper={upper}")
        # if no root
        if not node:
            return True

        # if node's val is outside the calculated bound
        if (lower is not None and node.val <= lower) or (
            upper is not None and node.val >= upper
        ):
            return False

        # calculating bounds for left and right nodes
        left_subtree = self.isValid(node.left, lower, node.val)
        right_subtree = self.isValid(node.right, node.val, upper)

        return left_subtree and right_subtree

    def isValidBST(self, root) -> bool:
        """
        Approach: based on a comparison between lower and upper bound of node with its left and right subtree, check notebook for more info
        """
        return self.isValid(root, None, None)


nodeB = TreeNode(-1)
root = TreeNode(0, None, nodeB)

sol = Solution()
result = sol.isValidBST(root)

if result:
    print("VALID BST")
else:
    print("NOT A VALID BST")
