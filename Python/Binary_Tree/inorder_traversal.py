# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorder(self, node, ans):
        if node:
            self.inorder(node.left, ans)
            ans.append(node.val)
            self.inorder(node.right, ans)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Traversed left subtree then visit current node then traverse right subtree
        """
        ans = []
        self.inorder(root, ans)
        return ans
