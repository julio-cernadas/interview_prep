# CHAPTER 4: BACKTRACKING AND TREE TRAVERSAL ALGORITHMS

# EXPLANATION:
# What is the base case?
# A leaf node with no children, which by its nature has a depth of one level.

# What argument is passed to the recursive function call?
# The node whose greatest depth we want to find.

# How does this argument become closer to the base case?
# A DAG has no cycles, so following the descendant nodes will eventually reach a leaf node.


root = {
    "data": "A",
    "children": [
        {
            "data": "X",
            "children": [
                {
                    "data": "D",
                    "children": [],
                },
            ],
        },
        {
            "data": "C",
            "children": [
                {
                    "data": "E",
                    "children": [
                        {
                            "data": "G",
                            "children": [],
                        },
                        {
                            "data": "H",
                            "children": [],
                        },
                    ],
                },
                {
                    "data": "F",
                    "children": [],
                },
            ],
        },
    ],
}


def max_depth(node):
    # BASE CASE
    if not node["children"]:
        return 0

    # RECURSIVE CASE
    max_child_depth = 0
    for child in node["children"]:
        child_depth = max_depth(child)
        if child_depth > max_child_depth:
            max_child_depth = child_depth

    return max_child_depth + 1


print(max_depth(root))
