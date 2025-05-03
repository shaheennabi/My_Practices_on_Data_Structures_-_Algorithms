
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next



class Solution:
    def middle_of_linkedlist(head):
        
        if not head or head.next:  # here we are checking if the head and it's next node is empty
            return head
        
        slow_pointer = head  # slow will start from head
        fast_pointer = head  # fast will also start from head

        while fast_pointer and fast_pointer.next:  #until fast pointer and it's next exists, if fast_pointer.next = None it will come out of loop. till we will get middle
            slow_pointer = slow_pointer.next   # slow pointer will move one step
            fast_pointer = fast_pointer.next.next  # fast pointer will move two steps at a time, when it will reach end, we will get the slow pointer at middle 

        return slow_pointer  # returning the middle by slow pointer
        