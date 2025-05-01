class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def remove_duplicates_from_sorted_lists(self, head):
        if not head:   # first we are checking if the linkedlist is empty, if it's return head
            return head
        
        current = head   #current will start from first node

        while current and current.next:  # until current and it's next exist
            if current.val == current.next.val:  # check if current and it's next node's value is equal
                current.next = current.next.next   #if yes then current's next will be it's next -> next
            else:
                current = current.next  #otherwise current will move further

        return head  #returning the non-duplicate list