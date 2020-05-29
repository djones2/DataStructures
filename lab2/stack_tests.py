import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
#from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)   
        with self.assertRaises(IndexError):  
            stack.pop()
        with self.assertRaises(IndexError):  
            stack.peek()
        self.assertTrue(stack.is_empty())
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(stack.size(),5)
        with self.assertRaises(IndexError):  
            stack.push(5)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.size(),4)
        self.assertEqual(stack.peek(), 3)

if __name__ == '__main__': 
    unittest.main()
