# EXPLANATION:
# The nodes are always traversed in the same order for both...
# We go down the child nodes first (called a depth-first search) as opposed to visiting the nodes in each
# level before going deeper (called a breadth-first search). The pre and post refer to when the node’s data
# is accessed: either before or after traversing the node’s children.


root = {
    "data": "A",
    "children": [
        {"data": "B", "children": [{"data": "D", "children": []}]},
        {
            "data": "C",
            "children": [
                {"data": "E", "children": [{"data": "G", "children": []}, {"data": "H", "children": []}]},
                {"data": "F", "children": []},
            ],
        },
    ],
}


def pre_order_traversal(node):
    # Access this node's data
    print(node["data"], end=" ")

    # RECURSIVE CASE
    for child in node["children"]:
        # Traverse child nodes
        pre_order_traversal(child)

    # BASE CASE
    return


def post_order_traversal(node):
    # RECURSIVE CASE
    for child in node["children"]:
        # Traverse child nodes
        post_order_traversal(child)

    # Access this node's data
    print(node["data"], end=" ")

    # BASE CASE
    return


pre_order_traversal(root)
print("\n")
post_order_traversal(root)
