# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.answer = []

    # does pre-order traversal
    def find_path(self, node, sum_till_parent, path_till_parent, target_sum):
        if node:
            # evaluate sum till parent node
            sum_till_me = sum_till_parent + node.val
            path_till_parent.append(node.val)

            # when node is leaf node and target equals running sum
            if not node.left and not node.right and sum_till_me == target_sum:
                current_path = []
                for i in path_till_parent:
                    current_path.append(i)

                # populate the answer list with [[path_values], [path_values2],...]
                self.answer.append(current_path)

            if node.left:
                self.find_path(node.left, sum_till_me, path_till_parent, target_sum)

            if node.right:
                self.find_path(node.right, sum_till_me, path_till_parent, target_sum)

            # for ignoring any side-effect
            path_till_parent.pop(-1)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        sum_till_parent = 0
        self.find_path(root, sum_till_parent, path, targetSum)
        return self.answer
