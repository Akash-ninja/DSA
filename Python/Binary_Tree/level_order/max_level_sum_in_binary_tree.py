# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Approach: using level order traversal calculating level and its sum
        """
        if not root:
            return 0

        queue = deque()  # create queue
        queue.append({"level": 1, "node": root})

        obj = dict()
        while queue:
            # dequeue from the queue
            node_info = queue.popleft()
            level = node_info.get("level")
            node = node_info.get("node")

            # process nodes in that level
            if level not in obj:
                obj[level] = node.val
            else:
                obj[level] += node.val

            # traversal
            if node.left:
                queue.append({"level": level + 1, "node": node.left})
            if node.right:
                queue.append({"level": level + 1, "node": node.right})

        # find level that holds max. sum
        result = 1
        for key, value in obj.items():
            if value > obj.get(result):
                result = key

        return result
