class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        pass

    def f(self, node):
        if not node:
            return {"diameter": 0, "height": 0}
        else:
            left = self.f(node.left)
            right = self.f(node.right)

            height = max(left["height"], right["height"]) + 1
            diameter = max(
                max(left["diameter"], right["diameter"]),
                left["height"] + right["height"],
            )
            return {"diameter": diameter, "height": height}

    def find_diameter(self, root):
        my_dict = self.f(root)
        diameter, height = my_dict.values()
        print(f"Diameter of the tree = {diameter},\nHeight of the tree = {height}")
        return (diameter, height)


nodeD = TreeNode(5)
nodeC = TreeNode(4)
nodeA = TreeNode(2)
nodeB = TreeNode(3)

root = TreeNode(1, nodeA, nodeB)

nodeA.left = nodeC
nodeA.right = nodeD


sol = Solution()
sol.find_diameter(root)
