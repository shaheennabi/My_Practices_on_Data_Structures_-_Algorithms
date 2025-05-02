### Solution 1 to store values in array and later check it in reverse order if they are same
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def check_palindrome(self, head):
        values = []  # empty list to save values
        current = head  # current will traverse from head

        while current:   # until current exists
            values.append(current.val)  # every current value will be appended to empty list
            current = current.next  # move current forward
        
        return values == values[::-1]    # return True if appended values and it's reverse is same


