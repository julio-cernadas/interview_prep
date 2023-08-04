# Input:    [1,2,3,4,5]
# Output:   [5,4,3,2,1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(node):
    if node is None or node.next is None:
        return node

    reversed_node = reverse_list(node.next)
    node.next.next = node
    node.next = None
    return reversed_node


data = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
output = reverse_list(data)
print(output)
