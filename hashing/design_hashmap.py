class MyHashMap(object):
    def __init__(self):
        # Initialize an array of size 1,000,001 with all values set to -1.
        # This array will act as the storage for the HashMap.
        # Each index represents a possible key, and the value at that index is the stored value.
        self.arr = [-1] * 1000001

    def put(self, key, value):
        # Store the value at the index equal to the key.
        # If the key already exists, it will update the value.
        self.arr[key] = value

    def get(self, key):
        # Return the value at the index equal to the key.
        # If the key doesn't exist (i.e., was never set or was removed), it will return -1.
        return self.arr[key]

    def remove(self, key):
        # Set the value at the index equal to the key back to -1,
        # indicating that the key has been removed.
        self.arr[key] = -1
