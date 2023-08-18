class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root, p, q):
    # Step 1: Base case - return root if root is None or matches either p or q
    if not root or root == p or root == q:
        return root

    # Step 2: Recurse on the left subtree
    left_lca = lowest_common_ancestor(root.left, p, q)

    # Step 3: Recurse on the right subtree
    right_lca = lowest_common_ancestor(root.right, p, q)

    # Step 4: If both left and right subtrees have a valid LCA, return the current root
    if left_lca and right_lca:
        return root

    # Step 5: Return the valid LCA from either subtree
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
