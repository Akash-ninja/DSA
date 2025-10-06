# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.ans = -1

    def inorder(self, node, k):
        if node:
            if node.left:
                self.inorder(node.left, k)

            self.count += 1
            if self.count == k:
                self.ans = node.val
                return self.ans

            if node.right:
                self.inorder(node.right, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Approach: Inorder traversal in BST gives k-th smallest element
        """
        self.inorder(root, k)
        return self.ans