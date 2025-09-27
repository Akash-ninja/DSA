# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    pre_order_index = 0
    inorder_map = dict()

    # pre-order traversal
    def construct_binary_tree(self, preorder, inorder, index_start, index_end):
        if index_start > index_end:
            return None

        root_value = preorder[self.pre_order_index]
        root_index = self.inorder_map.get(root_value)

        node = TreeNode(root_value)

        self.pre_order_index += 1

        node.left = self.construct_binary_tree(
            preorder, inorder, index_start, root_index - 1
        )
        node.right = self.construct_binary_tree(
            preorder, inorder, root_index + 1, index_end
        )
        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Algo:
            pre-algo step: create map so that root value and index can be found easily
            1. Search root node (in preorder list)
            2. Search root index (in inorder list)
            3. create node
            4. increment search index tracker in preorder (pre_order_index)
            5. --Recursively create left and right subtree (repeatition)
            6. return node
        """
        for i in range(0, len(inorder)):
            self.inorder_map[inorder[i]] = i

        return self.construct_binary_tree(preorder, inorder, 0, len(inorder) - 1)
