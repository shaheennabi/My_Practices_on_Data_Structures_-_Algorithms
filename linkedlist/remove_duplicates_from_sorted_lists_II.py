class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def remove_duplicates_from_sorted_list_II(self, head):
        # Create a dummy node with value 0 to handle edge cases easily
        fake = ListNode(0)
        fake.next = head

        # prev points to the last node before the group of duplicates (initially dummy)
        prev = fake

        # current pointer to traverse the list
        current = head

        while current and current.next:
            if current.val == current.next.val:
                # We found the beginning of duplicates
                duplicate_value = current.val

                # -------------------- BIG COMMENT --------------------
                # This loop skips all the nodes that have the same value as duplicate_value.
                # For example, in a list like: 1 → 2 → 3 → 3 → 3 → 4
                # When current is at the first '3', we want to skip *all* '3's.
                # So we keep moving current forward as long as current exists
                # and its value is equal to duplicate_value.
                # After the loop, current will point to the first node with a different value (e.g., 4)
                # or to None if we reached the end of the list.
                # -----------------------------------------------------
                while current and current.val == duplicate_value:
                    current = current.next

                # Link the last unique node (prev) to the node after all duplicates
                prev.next = current

            else:
                # If current and next node are not duplicates,
                # move both pointers forward
                prev = current
                current = current.next

        # Return the next of dummy node (actual head after removing duplicates)
        return fake.next
