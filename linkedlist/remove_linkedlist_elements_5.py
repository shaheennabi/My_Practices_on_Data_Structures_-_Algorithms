class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def remove_elements(self, head, val):
        if not head:
            return head
        
        fake = ListNode()
        fake.next = head

        current = fake # starting from 0 the fake node
        
        while current.next:  # check till fake.next exists
            if current.next.val == val:  #if fakes next val = given val
                current.next = current.next.next  # then currents next will ignore next node
            else:
                current = current.next  # this will move step by step to traverse through all the nodes
        
        return fake.next  # thisd will return from ist index