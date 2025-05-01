class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        count = 0
        while current:
            if count == index - 1:
                new_node = Node(val)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            count += 1

    def deleteAtIndex(self, index):
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current and current.next:
            if count == index - 1:
                current.next = current.next.next
                return
            current = current.next
            count += 1
