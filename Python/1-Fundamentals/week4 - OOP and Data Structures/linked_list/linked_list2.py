class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def iter_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next

head = Node("1st node")
head.next = Node("2nd node")
head.next.next = Node("3rd node")
head.next.next.next = Node("4th node")
