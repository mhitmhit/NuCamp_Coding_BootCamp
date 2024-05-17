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


list1 = LinkedList()

list1.append("1st node")
list1.append("2nd node")
list1.append("3rd node")
list1.append("4th node")

list1.iter_linked_list()
