# EXPLANATION:
# Inorder traversal typically refers to the traversal of binary trees, although processing a node’s data after
# traversing the first node and before traversing the last node would count as inorder traversal for trees of any size.


root = {
    "data": "A",
    "children": [
        {"data": "Z", "children": [{"data": "D", "children": []}]},
        {
            "data": "C",
            "children": [
                {"data": "E", "children": [{"data": "G", "children": []}, {"data": "H", "children": []}]},
                {"data": "F", "children": []},
            ],
        },
    ],
}


def in_order_traverse(node):
    # RECURSIVE CASE
    # Traverse the left child.
    if len(node["children"]) >= 1:
        in_order_traverse(node["children"][0])

    # Access this node's data.
    print(node["data"], end=" ")

    # RECURSIVE CASE
    # Traverse the right child.
    if len(node["children"]) >= 2:
        in_order_traverse(node["children"][1])

    # BASE CASE
    return


in_order_traverse(root)
