class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node("1st node")
head.next = Node("2nd node")
head.next.next = Node("3rd node")
