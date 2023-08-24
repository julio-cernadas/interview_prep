# BIG O:
# O(n)

# EXPLANATION:
# Uses a recursive DFS approach to check if each node's value is within the valid range based on its position in the
# tree. The code also creates a simple binary tree, calls the function with the root, and prints the result.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root) -> bool:
    def dfs(lower, node, upper) -> bool:
        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        left_valid = dfs(lower, node.left, node.val)
        right_valid = dfs(node.val, node.right, upper)
        return left_valid and right_valid

    is_valid = dfs(float("-inf"), root, float("inf"))
    return is_valid


data = TreeNode(2, TreeNode(1), TreeNode(3))
output = is_valid_bst(data)
print(output)
