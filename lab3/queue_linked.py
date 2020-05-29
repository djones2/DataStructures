class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        self.front = None
        self.rear = None
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.front == None:
            return True
        else:
            return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items == self.capacity:
            return True
        else:
            return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.is_full():
            raise IndexError
        new = Node(item)
        self.num_items += 1
        if self.front == None:
            self.front = new
        elif self.rear == None:
            self.rear = new
            self.front.next = self.rear
        else:
            self.rear.next = new
            self.rear = new

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.is_empty():
            raise IndexError
        temp = self.front.data
        self.front = self.front.next
        self.num_items -= 1
        return temp

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
    
    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.front.data
