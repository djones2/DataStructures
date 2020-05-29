class Node:
    '''Node for use with doubly-linked list'''

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           Do not have an attribute to keep track of size'''
        self.sentinel = Node(None)

    def is_empty(self):
        '''Returns back True if OrderedList is empty
            MUST have O(1) performance'''
        if self.sentinel.next == None:
            return True
        else:
            return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           If the item is already in the list, do not add it again 
           MUST have O(n) average-case performance'''
        new = Node(item)
        # Add to empty list
        if self.sentinel.next == None:
            self.sentinel.next = new
            new.prev = self.sentinel
            if self.sentinel.prev == None:
                new.next = self.sentinel
                self.sentinel.prev = new
        # Add to front of list
        elif new.item < self.sentinel.next.item:
            current = self.sentinel.next.prev = new
            new.next = self.sentinel.next
            new.prev = self.sentinel
            self.sentinel.next = new
        # Add to back of list
        elif new.item > self.sentinel.prev.item:
            self.sentinel.prev.next = new
            new.prev = self.sentinel.prev
            self.sentinel.prev = new
            new.next = self.sentinel
        # Add somewhere inside list
        else:
            prev = self.sentinel
            current = self.sentinel.next
            while current is not self.sentinel or current.item == new.item:
                if new.item < current.item and new.item > prev.item:
                    new.prev = prev
                    new.next = current
                    prev.next = new
                    current.prev = new
                    return
                prev = current
                current = current.next

    def remove(self, item):
        '''Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        prev = self.sentinel
        current = self.sentinel.next
        if current == None:
            return False
        # First item removal
        if item == current.item:
            if current.next == self.sentinel:
                self.sentinel.next = None
                self.sentinel.prev = None
            else:
                self.sentinel.next = current.next
                current.next.prev = self.sentinel
            return True
        # Last item removal
        elif item == prev.prev.item:
            prev.prev.prev.next = prev
            prev.prev = prev.prev.prev
            return True
        elif prev.prev.item > item > current.item:
            while current != self.sentinel:
                if item == current.item:
                    prev.next = current.next
                    current.next.prev = prev
                    return True
                prev = current
                current = current.next
        else:
            return False

    def index(self, item):
        '''Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        index = 0
        current = self.sentinel.next
        while current is not self.sentinel:
            if current.item == item:
                return index
            current = current.next
            index += 1
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0 or index > self.size():
            raise IndexError
        current = self.sentinel.next
        count = 0
        while (count - 1) != index:
            result = current.item
            current = current.next
            count += 1
        return result

    def search_help(self, item, current):
        if current == self.sentinel:
            return False
        if current.item == item:
            return True
        return self.search_help(item, current.next)

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        if self.is_empty() == True:
            return False
        current = self.sentinel.next
        return self.search_help(item, current)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        if self.is_empty() == True:
            return []
        current = self.sentinel.next
        result = [None] * self.size()
        index = 0
        while current != self.sentinel:
            result[index] = current.item
            current = current.next
            index += 1
        return result

    def reverse_help(self, list, item, index):
        list[-index] = item.item
        if item.next == self.sentinel:
             return list
        return self.reverse_help(list, item.next, index + 1)

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        if self.is_empty():
            return None
        current = self.sentinel.next
        result = [None] * self.size()
        return self.reverse_help(result, current, 1)

    def get_size(self, current, size):
        size += 1
        if current.next == self.sentinel:
            return size
        return self.get_size(current.next, size)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        if self.is_empty() == True:
            return 0
        current = self.sentinel.next
        return self.get_size(current, 0)

