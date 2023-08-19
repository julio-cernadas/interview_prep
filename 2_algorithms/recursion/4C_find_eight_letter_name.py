# CHAPTER 4: BACKTRACKING AND TREE TRAVERSAL ALGORITHMS

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
        {
            "name": "Bob",
            "children": [
                {"name": "Darya", "children": []},
            ],
        },
        {
            "name": "Caroline",
            "children": [
                {
                    "name": "Eve",
                    "children": [
                        {"name": "Gonzaloe", "children": []},
                        {"name": "Hadassah", "children": []},
                    ],
                },
                {"name": "Fred", "children": []},
            ],
        },
        {"name": "Jeff", "children": [{"name": "Jane", "children": []}]},
    ],
}


def find_eight_letter_name(node_tree):
    def dfs(node):
        # BASE CASE
        if len(node["name"]) == 8:
            result.append(node["name"])

        # RECURSIVE CASE
        for child in node["children"]:
            dfs(child)

    result = []
    dfs(node_tree)
    return result


print(find_eight_letter_name(root))
