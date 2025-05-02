class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def intersection_of_two_linkedlist(self, headA, headB):
        if not headA or headB: # first check if either linkedlist is empty
            return None
        
        a_pointer = headA   
        b_pointer = headB

        while a_pointer != b_pointer:  #checking till a_pointer not equals b_pointer
            a_pointer = a_pointer.next if a_pointer else headB  # here if a_pointer is not None move forward, if none push to head of B
            b_pointer = b_pointer.next if b_pointer else headA  # here if b_pointer is not None move forward, if none push to headA
        
        return a_pointer   #returning the node val where they Intersect or None