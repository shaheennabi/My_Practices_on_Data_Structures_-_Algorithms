class Node:
    def __init__(self, val):
        self.val = val       # Store the value
        self.next = None     # Initialize next pointer to None

class LinkedList:
    def __init__(self):
        self.head = None     # Head initially points to None (empty list)
        self.size = 0        # Track size of the linked list

    def get_value(self, index):
        # If list is empty or index is invalid
        if self.head is None or index >= self.size:
            return -1

        count = 0
        current = self.head

        while current:
            if count == index:
                return current.val
            current = current.next
            count += 1

        return -1   # If somehow not found (edge case, but safe)

    