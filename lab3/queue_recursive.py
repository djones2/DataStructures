class Queue:
    def __init__(self, value):
        self.value = value
        self.rest = None

    def enqueue(self, item):
        pass
       

    def dequeue(self):
        temp = self.value
        self.value = self.rest.value
        self.rest = self.rest.rest
        return temp

if __name__ == '__main__':
    q = Queue(5)
    q.enqueue(2)
    q.enqueue(9)
    q.enqueue(1)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())