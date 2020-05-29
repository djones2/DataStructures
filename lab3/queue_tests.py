import unittest
from queue_array import Queue
#from queue_linked import Queue


class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)   
        with self.assertRaises(IndexError):  
            q.dequeue()
        with self.assertRaises(IndexError):  
            q.peek()
        self.assertTrue(q.is_empty())
        q.enqueue(0)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.peek(), 0)
        self.assertEqual(q.size(),5)
        with self.assertRaises(IndexError):  
            q.enqueue(5)
        self.assertTrue(q.is_full())
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.size(),4)


if __name__ == '__main__':
    unittest.main()
