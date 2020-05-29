class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type 
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.front = 0
        self.back = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.front == self.back:
            return True
        else:
            return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.items[self.back % self.capacity] is not None:
            return True
        else:
            return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full():
            raise IndexError
        self.items[self.back  % self.capacity] = item
        self.back = (self.back + 1)

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty():
            raise IndexError
        item = self.items[self.front % self.capacity]
        self.items[self.front % self.capacity] = None
        self.front = (self.front + 1)
        return item

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.back - self.front

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.items[self.front]