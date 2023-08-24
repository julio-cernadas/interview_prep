# BIG O:
# O(n)

# EXPLANATION:
# Inverts the entire tree by swapping the left and right subtrees of each node, starting from the root and going
# recursively down the tree. The function then returns the new root of the inverted tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root
