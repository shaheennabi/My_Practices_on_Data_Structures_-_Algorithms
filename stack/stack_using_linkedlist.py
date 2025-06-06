class Node:

    def __init__(self, value):
        self.data = value
        self.next = None
        

class Stack:

    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None

    def push(self, value):

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def traversal(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

    def peek(self):
        if (self.isempty()):
            return "Stack Empty"
        else: 
            return self.top.data

    def pop(self):
        if (self.isempty()):
            return "Stack Empty"
        else:
            self.top = self.top.next