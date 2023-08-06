class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_best(root) -> bool:
    return dfs(root, float("-inf"), float("inf"))


def dfs(node, lower, upper) -> bool:
    if not node:
        return True

    if not (lower < node.val < upper):
        return False

    left_valid = dfs(node.left, lower, node.val)
    right_valid = dfs(node.right, node.val, upper)

    if not (left_valid and right_valid):
        return False

    return True


data = TreeNode(2, TreeNode(1), TreeNode(3))
output = is_valid_best(data)
print(output)
