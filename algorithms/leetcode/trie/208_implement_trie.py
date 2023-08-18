class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["EOF"] = {}

    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]

        is_end = "EOF" in node
        return is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True


obj = Trie()
data = "apple"
obj.insert(data)
param_2 = obj.search(data)
param_3 = obj.starts_with("app")
