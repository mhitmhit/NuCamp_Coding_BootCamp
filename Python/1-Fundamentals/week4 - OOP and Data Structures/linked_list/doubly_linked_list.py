class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None

class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head node created: ", self.head.value)
            return
        new_node.pre = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", new_node.pre.value)

    def iterate_forward(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def iterate_backward(self):
        node = self.tail
        while node is not None:
            print(node.value)
            node = node.pre



mylist = Doubly_linked_list()
mylist.append("1st node")
mylist.append("2nd node")
mylist.append("3rd node")
mylist.append("4th node")
mylist.append("5th node")
print("--------------------------forward---")
mylist.iterate_forward()
print("---------------------------backwards--")
mylist.iterate_backward()
