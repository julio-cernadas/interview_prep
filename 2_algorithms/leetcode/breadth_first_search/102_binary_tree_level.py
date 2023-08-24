# BIG O:
# O(n)

# EXPLANATION:
# Performs a level-order traversal on a binary tree and returns the values of nodes at each level in a nested list
# format. It uses a queue to manage nodes at each level and efficiently constructs the result using nested lists.


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    visited = []
    queue = [[root]]

    while queue:
        sub_visited = []
        sub_queue = []

        level = queue.pop(0)
        for node in level:
            if hasattr(node, "left"):
                sub_queue.append(node.left)

            if hasattr(node, "right"):
                sub_queue.append(node.right)

            if hasattr(node, "val"):
                sub_visited.append(node.val)

        if sub_visited:
            visited.append(sub_visited)
        if sub_queue:
            queue.append(sub_queue)

    return visited


data = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
output = level_order(data)
print(output)
