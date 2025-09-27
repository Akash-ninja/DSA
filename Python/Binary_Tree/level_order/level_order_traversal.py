# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# not to do in leetcode
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Approach: using Deque (double ended queue) operations: - append() and popleft()

        """
        if not root:
            return []

        ans = list()
        queue = deque()  # create queue
        queue.append(root)  # insert root node

        while queue:
            level = list()  # to take no. of nodes in a level
            n = len(queue)

            for _ in range(n):
                node = queue.popleft()  # pop the node from queue
                level.append(node.val)  # processing the popped node

                if node.left:
                    queue.append(node.left)  # traverse left
                if node.right:
                    queue.append(node.right)  # traverse right

            ans.append(level)

        return ans
