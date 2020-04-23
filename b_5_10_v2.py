class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next  = next

    def __str__(self):
        return str(self.value)

    def print_reverse_node(self):
        if self.next != None:
            tail = self.next
            tail.print_reverse_node()
        print (self.value, end = " ")

class LinkedList():
    def __init__(self):
        self.length = 0
        self.head = None

    def print_reverse_list(self):
        print ("[", end = " ")
        if self.head != None:
            self.head.print_reverse_node()
        print ("]")

    def add_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

linkedlist = LinkedList()
linkedlist.add_first(1)
linkedlist.add_first(2)
linkedlist.add_first(3)
linkedlist.print_reverse_list()