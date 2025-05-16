class Node:
    def __init__(self, value):
        self.data = value
        self.next = None 

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):

        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front 
        else:
            self.rear.next = new_node
            self.rear = new_node
            
            
    def dequeue(self):

        if self.front == None:
            return "Empty"
        else:
            self.front = self.front.next

    def traverse(self):

        temp = self.front

        while temp != None:
            print(temp.data)
            temp = temp.next 

    def is_empty(self):
        return self.front == None

    def size(self):
        temp = self.front
        counter = 0
        while temp != None:
            temp += 1
            counter +=1
        return counter

    def front_item(self):
        if self.front == None:
            return "Empty"
        else: 
            return self.front.data

    def rear_item(self):
        if self.front == None:
            return "Empty"
        else:
            return self.rear.data