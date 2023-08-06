def new_node(key):
    return {"key": key, "left": None, "right": None}


def insert(key, root=None):
    if not root:
        return new_node(key)

    if key < root["key"]:
        root["left"] = insert(key, root["left"])
    elif key > root["key"]:
        root["right"] = insert(key, root["right"])

    return root


def search(key, root=None):
    if not root:
        return False

    if key == root["key"]:
        return True
    elif key < root["key"]:
        return search(key, root["left"])
    else:
        return search(key, root["right"])


def validate(root):
    res = []
    if root:
        res = validate(root["left"])
        res.append(root["key"])
        res = res + validate(root["right"])
    return res


bst_root = None
values_to_insert = [50, 30, 70, 20, 40, 60, 80]
for val in values_to_insert:
    bst_root = insert(val, bst_root)

print(search(25, bst_root))
print(search(40, bst_root))
print(validate(bst_root))
