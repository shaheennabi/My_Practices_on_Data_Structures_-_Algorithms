class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Linkedlist: 
    def __init__(self):
        self.head = None
        self.size = 0 

    def delete_At_index(self, index):
        if not self.head:
            return 
         
        if index == 0:
            self.head = self.head.next 
            size -= 1
            return 
        
        count = 0
        current = self.head

        while current and current.next:
            if count == index - 1:
                current.next = current.next.next
                size -= 1
                return 
            current = current.next 
            count += 1 
        return -1 