# EXPLANATION:
# Instead of printing out the data in each node as we traverse them,
# we can use a depth-first search to find specific data in a tree data structure

# What is the base case?
# Either a leaf node causing the algorithm to backtrack, or a node containing an eight-letter name.

# What argument is passed to the recursive function call?
# The node to traverse to, whose child nodes will be the next nodes to traverse.

# How does this argument become closer to the base case?
# There are no cycles in a DAG, so following the descendant nodes will always eventually reach a leaf node.

root = {
    "name": "Alice",
    "children": [
        {"name": "Bob", "children": [{"name": "Darya", "children": []}]},
        {
            "name": "Caroline",
            "children": [
                {
                    "name": "Eve",
                    "children": [{"name": "Gonzalo", "children": []}, {"name": "Hadassah", "children": []}],
                },
                {"name": "Fred", "children": []},
            ],
        },
    ],
}


def find_eight_letter_name(node):
    # Preorder depth-first search:
    # BASE CASE
    if len(node["name"]) == 8:
        return node["name"]

    # RECURSIVE CASE
    if len(node["children"]) > 0:
        for child in node["children"]:
            return_value = find_eight_letter_name(child)
            if return_value is not None:
                return return_value

    # Postorder depth-first search:
    # BASE CASE
    # if len(node['name']) == 8:
    #     return node['name']

    # BASE CASE
    # Value was not found or there are no children.
    return None


print(find_eight_letter_name(root))
