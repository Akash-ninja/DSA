# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def find_diameter(self, node):
        if not node:
            return {"diameter": 0, "height": 0}
        else:
            left = self.find_diameter(node.left)
            right = self.find_diameter(node.right)

            height = max(left["height"], right["height"]) + 1
            diameter = max(
                max(left["diameter"], right["diameter"]),
                left["height"] + right["height"],
            )
            return {"diameter": diameter, "height": height}

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        tree_details = self.find_diameter(root)
        diameter, height = tree_details.values()
        return diameter
