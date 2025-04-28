class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_At_tail(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node  
            self.size += 1
            return 
        
        current = self.head
        while current.next:    
            current = current.next   
        
        current.next = new_node     
        self.size += 1              
