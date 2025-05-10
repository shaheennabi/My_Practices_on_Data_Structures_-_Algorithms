class Dictionary:
    def __init__(self, size):
        # Initialize dictionary with fixed size
        self.size = size
        self.slots = [None] * self.size  # Stores keys
        self.data = [None] * self.size   # Stores values corresponding to keys

    def put(self, key, value):
        """
        Insert a key-value pair into the dictionary.
        Uses linear probing in case of collision.
        """
        hash_value = self.hash_function(key)

        # If slot is empty, insert the key and value
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value

        # If the same key exists, update its value
        elif self.slots[hash_value] == key:
            self.data[hash_value] = value

        else:
            # Collision and different key: use linear probing
            new_hash_value = self.rehash(hash_value)

            # Probe until an empty slot or the same key is found
            while self.slots[new_hash_value] is not None and self.slots[new_hash_value] != key:
                new_hash_value = self.rehash(new_hash_value)

            # Insert in empty slot
            if self.slots[new_hash_value] is None:
                self.slots[new_hash_value] = key
                self.data[new_hash_value] = value
            else:
                # Update value if key already exists
                self.data[new_hash_value] = value

    def get(self, key):
        """
        Retrieve the value associated with the key.
        Returns 'Not Found' if key does not exist.
        """
        start_position = self.hash_function(key)
        current_position = start_position

        # Loop to find the key using linear probing
        while self.slots[current_position] is not None:
            if self.slots[current_position] == key:
                return self.data[current_position]
            
            current_position = self.rehash(current_position)

            # Full loop done without finding the key
            if current_position == start_position:
                return "Not Found"
        
        return "Not Found"

    def __str__(self):
        """
        String representation of the dictionary.
        """
        output = []
        for i in range(len(self.slots)):
            if self.slots[i] is not None:
                output.append(f"{self.slots[i]}: {self.data[i]}")
        return ", ".join(output)

    def __getitem__(self, key):
        # Enables dictionary-style access (dict[key])
        return self.get(key)

    def __setitem__(self, key, value):
        # Enables dictionary-style setting (dict[key] = value)
        self.put(key, value)

    def rehash(self, old_hash):
        # Linear probing: move to the next slot
        return (old_hash + 1) % self.size

    def hash_function(self, key):
        # Hash function using built-in hash and modulo for indexing
        return abs(hash(key)) % self.size



D1 = Dictionary(3)
print(D1.slots)
print(D1.data)