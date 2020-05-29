
class MaxHeap:

    def __init__(self, capacity=50):
        """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
        self.max_capacity = capacity
        self.heap_list = [None] * (capacity + 1)
        self.size = 0

    def enqueue(self, item):
        """inserts "item" into the heap, returns true if successful, false if there is no room in the heap"""
        if self.is_full():
            return False
        elif self.size == 0:
            self.heap_list[1] = item
            self.size +=  1
            return True
        else:
            self.heap_list.insert(self.size + 1, item)
            self.size += 1
            self.perc_up(self.size)
            return True

    def peek(self):
        """returns max without changing the heap, returns None if the heap is empty"""
        return self.heap_list[1]

    def dequeue(self):
        """returns max and removes it from the heap and restores the heap property
           returns None if the heap is empty"""
        if self.is_empty():
            return None
        else:
            retval = self.heap_list[1]
            self.heap_list[1] = self.heap_list[self.size]
            self.size -= 1
            self.heap_list.pop()
            self.perc_down(1)
            return retval
            

    def contents(self):
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)"""
        contents = []
        for i in range(0, self.get_size()):
            contents.append(self.heap_list[i+1])
        return contents

    def build_heap(self, alist):
        """Builds a heap from the items in alist and builds a heap using the bottom up method.  
        If the capacity of the current heap is less than the number of 
        items in alist, the capacity of the heap will be increased"""
        i = len(alist) // 2
        self.size = len(alist)
        self.heap_list = [0] + alist[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1
        #return True

    def is_empty(self):
        """returns True if the heap is empty, false otherwise"""
        if self.size == 0:
            return True
        else:
            return False

    def is_full(self):
        """returns True if the heap is full, false otherwise"""
        if self.size == self.capacity():
            return True
        else:
            return False

    def capacity(self):
        """this is the maximum number of a entries the heap can hold
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.max_capacity

    def get_size(self):
        """the actual number of elements in the heap, not the capacity"""
        return self.size

    def perc_down(self, i):
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i * 2) <= self.size:
            mc = self.maxChild(i)
            if self.heap_list[i] < self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc
    

    def maxChild(self,i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap_list[i*2] > self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1


    def perc_up(self, i):
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2


    def heap_sort_ascending(self, alist):
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, then mutate alist to put the items in ascending order"""
        length = len(alist)
        self = MaxHeap(length)
        self.build_heap(alist)
        for i in range(length - 1, -1, -1):
            alist[i] = self.dequeue()
        return alist


# class MinHeapTernary:

#     def __init__(self, capacity=50):
#         """Constructor creating an empty heap with default capacity = 50 but allows heaps of other capacities to be created."""
#         self.heap = [None]*(capacity + 1)
#         self.size = 0
 
#     def perc_down(self, i):
#         """where the parameter i is an index in the heap and perc_down moves the element stored
#         at that location to its proper place in the heap rearranging elements as it goes."""
#         while (i * 3 - 1) <= self.size:
#             mc = self.minChild(i)
#             if self.heap[i] > self.heap[mc]:
#                 tmp = self.heap[i]
#                 self.heap[i] = self.heap[mc]
#                 self.heap[mc] = tmp
#             i = mc

#     def minChild(self,i):
#         if i * 3 + 1 <= self.size:
#             if self.heap[i*3] < self.heap[(i*3)-1] and self.heap[i*3] < self.heap[(i*3)+1]:
#                 return i * 3
#             elif self.heap[(i*3)-1] < self.heap[(i*3)] and self.heap[(i*3)-1] < self.heap[(i*3)+1]:
#                 return i * 3 - 1
#             else:
#                 return i * 3 + 1
#         elif i * 3 <= self.size:
#             if self.heap[i*3] < self.heap[(i*3)-1]:
#                 return i * 3
#             else:
#                 return i * 3 - 1
#         else:
#             return (i * 3) - 1


# if __name__ == "__main__":
#     test_heap = MinHeapTernary(8)
#     content = [50, 6, 7, 9, 5, 8, 1]
#     for i in range(1,7):
#         test_heap.heap[i] = content[i]
#         test_heap.size += 1
#     test_heap.perc_down(1)
#     result = [6,1,7,9,5,8,50]
#     print(test_heap.heap)
#     # for i in range(1,8):
#     #     self.assertEqual(test_heap.heap[i], result[i])