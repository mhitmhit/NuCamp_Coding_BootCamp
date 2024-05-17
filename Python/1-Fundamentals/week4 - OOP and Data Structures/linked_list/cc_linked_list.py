class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def iter_linked_list(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print("Head node created: ", self.head.value)
            return
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print("Head node created: ", self.head.value)
            return

        new_node.next = self.head
        self.head = new_node
        print("Prepend new head node with value: ", self.head.value)
        print("node following head is:", self.head.next.value)


llist = LinkedList()

llist.prepend("First Node")
llist.prepend("Inserted New First Node")
