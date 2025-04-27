class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0 

    
    def add_At_head(self, val):
        if self.head is None:    # this  will  first check if the head is linkedlist is empty then new node will be head(that is it)
            new_node = Node(val)
            self.head = new_node
            self.size += 1 
            return 
        

        new_node = Node(val)
        new_node.next = self.head  # point new_node's next to old head
        self.head = new_node       # move head to new_node
        self.size += 1             # increment size

