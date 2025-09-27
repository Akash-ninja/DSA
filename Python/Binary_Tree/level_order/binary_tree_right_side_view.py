# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: please see level order traversal of binary tree
        """
        if not root:
            return []

        queue = deque()
        queue.append(root)
        result = list()

        while queue:
            n = len(queue)

            for i in range(n):
                node = queue.popleft()

                # if 'i' value is last value in that level then its the rightmost node
                if i == n - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
