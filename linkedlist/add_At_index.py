from linkedlist import add_At_head # importing head from another file
hd = add_At_head.LinkedList

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0 

    def add_At_index(self, index, val): # checking some cases 
        if index == 0:
            hd.add_At_head(val)
            return 
        if index >= self.size:
            return  -1
        
        count = 0
        current = self.head

        while current:             # checking if current is index - 1 then add new node
            if count == index - 1:
                new_node = Node(val)
                new_node.next = current.next
                current.next = new_node 
                self.size += 1
                return 
            
            current = current.next
            count += 1
            
