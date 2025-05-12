class MyHashSet(object):
    
    # Initialize the HashSet with a large array of False values.
    # This array will act as a direct-address table where the index is the key,
    # and the value (True or False) indicates whether the key is present in the set.
    def __init__(self):
        # Creating an array of size 1,000,001 initialized to False.
        # Each index of the array represents a potential key in the set.
        # The value at the index will be True if the key is added, otherwise False.
        self.a = [False] * 1000001

    # Add a key to the HashSet.
    # If the key is not already in the set, it is added and marked as True at its index.
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        # Mark the key as present by setting the corresponding index to True
        self.a[key] = True  # We are using the key as the index in the array.

    # Remove a key from the HashSet.
    # If the key exists, it is removed by setting the corresponding index to False.
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        # Mark the key as removed by setting the corresponding index to False
        self.a[key] = False  # This sets the index back to False, indicating key removal.

    # Check if a key is in the HashSet.
    # If the key exists, the value at its index will be True.
    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        # Return True if the key exists (a[key] is True), otherwise return False
        return self.a[key]  # Direct lookup to check if the key is in the set.

# Your MyHashSet object will be instantiated and called as follows:
# obj = MyHashSet()
# obj.add(key)      # Add key to the HashSet.
# obj.remove(key)   # Remove key from the HashSet.
# param_3 = obj.contains(key)   # Check if the key exists in the HashSet.
