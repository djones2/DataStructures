class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size  # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value):
        """ Inserts an entry into the hash table (using Horner hash function to 
        determine index, and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number 
        that the word appears on. If the key is not already in the table, then 
        the key is inserted, and the value is used as the first line number in 
        the list of line numbers. If the key is in the table, then the value is 
        appended to that key’s list of line numbers. If value is not used for a 
        particular hash table (e.g. the stop words hash table), can use the 
        default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size 
        should be increased (doubled + 1)."""
        index = self.horner_hash(key)
        self.insert_2(key, value, index)
        if self.get_load_factor() > 0.5:
            small_table = self.hash_table
            self.__init__(self.table_size * 2 + 1)
            for i in range(len(small_table)):
                item = small_table[i]
                if item == None:
                    continue
                else:
                    key = item[0]
                    values = item[1]
                    for val in values:
                        index = self.horner_hash(key)
                        self.insert_2(key, val, index)

    def insert_2(self, key, value, index):
        # Insert into empty slot
        if self.hash_table[index] == None:
            self.hash_table[index] = (key, [value])
            self.num_items += 1
            return
        # Additional line number
        elif self.hash_table[index][0] == key:
            self.hash_table[index][1].append(value)
            return
        # Collision
        else:
            self.collision_resolution(key, value, 0)

    def collision_resolution(self, key, value, collision_count):
        new_index = (self.horner_hash(key) +
                     (2**collision_count)) % self.table_size
        if self.hash_table[new_index] == None:
            self.hash_table[new_index] = (key, [value])
            self.num_items += 1
        elif self.hash_table[new_index][0] == key:
            self.hash_table[new_index][1].append(value)
        else:
            self.collision_resolution(key, value, collision_count + 1)

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        summation = min(len(key), 8)
        res = 0
        for i in range(summation):
            res += ord(key[i])*(31 ** (summation - 1 - i))
        return res % self.table_size

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        if self.get_index(key) == None:
            return False
        return True

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        index = self.horner_hash(key)
        return self.get_index_helper(key, index, 0)

    def get_index_helper(self, key, index, n):
        if self.hash_table[index] == None:
            return None
        elif self.hash_table[index][0] == key:
            return index
        index = (self.horner_hash(key) + (2**n)) % self.table_size
        return self.get_index_helper(key, index, n+1)

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        keys = []
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is not None:
                keys.append(self.hash_table[i][0])
        return keys

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        index = self.get_index(key)
        if index == None:
            return None
        return self.hash_table[index][1]

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items / self.table_size
