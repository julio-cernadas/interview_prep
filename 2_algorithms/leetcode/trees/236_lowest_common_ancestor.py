# BIG O:
# O(n)

# EXPLANATION:
# Recursively searches for the lowest common ancestor of p and q by traversing the tree. If the current node is None or
# equal to either p or q, it returns the current node as a potential common ancestor. Otherwise, it searches for the
# LCA in the left and right subtrees. If both subtrees contain non-None values, the current node is the LCA. If only
# one subtree contains a non-None value, that value is propagated up the recursion stack.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left_lca = lowest_common_ancestor(root.left, p, q)
    right_lca = lowest_common_ancestor(root.right, p, q)
    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca


node = TreeNode(3)
node.left = TreeNode(5)
node.right = TreeNode(1)
node.left.left = TreeNode(6)
node.left.right = TreeNode(2)
node.right.left = TreeNode(0)
node.right.right = TreeNode(8)
node.left.right.left = TreeNode(7)
node.left.right.right = TreeNode(4)

left_node = node.left
right_node = node.right
output = lowest_common_ancestor(node, left_node, right_node)
print(output.val)
