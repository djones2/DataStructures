import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.size(), 0)
        self.assertFalse(t_list.remove(10))
        self.assertFalse(t_list.search(99))
        self.assertEqual(t_list.python_list_reversed(), None)
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertTrue(t_list.remove(10))
        t_list.add(5)
        t_list.add(10)
        t_list.add(2)
        self.assertEqual(t_list.python_list(), [2, 5, 10])
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.index(10), 2)
        self.assertEqual(t_list.index(99), None)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.search(99))
        self.assertFalse(t_list.is_empty())
        self.assertFalse(t_list.remove(99))
        self.assertEqual(t_list.python_list_reversed(), [10, 5, 2])
        self.assertTrue(t_list.remove(10))
        self.assertEqual(t_list.pop(0), 2)
        with self.assertRaises(IndexError):  
            t_list.pop(-5)
        self.assertTrue(t_list.remove(5))
        self.assertFalse(t_list.remove(5))
        t_list.add(15)
        t_list.add(11)
        self.assertTrue(t_list.remove(2))
        t_list.add(2)
        self.assertTrue(t_list.remove(11))


if __name__ == '__main__': 
    unittest.main()
