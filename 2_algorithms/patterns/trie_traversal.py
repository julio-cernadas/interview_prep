class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True
        node.counter += 1

    def query(self, x):
        def dfs(node, prefix):
            if node.is_end:
                result.append((prefix + node.char, node.counter))

            for child in node.children.values():
                dfs(child, prefix + node.char)

        result = []
        root = self.root

        for char in x:
            if char in root.children:
                root = root.children[char]
            else:
                return []

        dfs(root, x[:-1])
        return sorted(result, key=lambda x: x[1], reverse=True)
