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

    if not root:
        return visited

    if not root.left and not root.right:
        visited.append([root.val])
        return visited

    while queue:
        node_level = queue.pop(0)
        visited_nodes = []
        queued_nodes = []
        for node in node_level:
            visited_nodes.append(node.val)

            if node.left:
                queued_nodes.append(node.left)

            if node.right:
                queued_nodes.append(node.right)

        visited.append(visited_nodes)
        if queued_nodes:
            queue.append(queued_nodes)

    return visited


data = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
output = level_order(data)
print(output)
