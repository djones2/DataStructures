import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """ Base case. Finds max integer in regular list """
        self.assertEqual(max_list_iter([1,2,3]), 3)

    def test_max_list_iter_empty_list(self):
        """ Passed empty list. Should return None. """
        self.assertEqual(max_list_iter([]), None)

    def test_max_list_iter_raise_valueerror(self):
        """Max list iteration test for list being None type and raising value error"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        """ Reversing a list. Base case. """
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec_empty(self):
        """ Reversing a list. Empty list. Returns empty list"""
        self.assertEqual(reverse_rec([]),[])

    def test_reverse_rec_long(self):
        """ Reversing a list. Long list."""
        self.assertEqual(reverse_rec([1, 2, 4, 5, 7, 8, 7, 4, 6, 7, 8]),[8, 7, 6, 4, 7, 8, 7, 5, 4, 2, 1])    

    def test_bin_search_low(self):
        """ Find a value between targets. Base case. Find known value in list.
            Low index holds target. """
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(2, low, high, list_val), 2 )

    def test_bin_search_high(self):
        """ Find a value between targets. Base case. Find known value in list.
            High index holds target. """
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(8, low, high, list_val), 6 )
    
    def test_bin_search_highest(self):
        """ Find a value between targets. Base case. Find known value in list.
            High index holds target. """
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(10, low, high, list_val), 8 )

    def test_bin_search_not_found(self):
        """ Find a value between targets. Target does not exist. Return None """
        list_val =[0,1,2,3,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(-2, low, high, list_val), None ) 

    def test_bin_search_target_out_of_index(self):
        """ Find a value between targets. Target is outside of low/high
        values. Return None """
        list_val =[0,1,2,3,4,7,8,9,10]
        low = len(list_val)-2
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), None )

    def test_bin_search_empty(self):
        """ Empty list, raise ValueError"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(4, 0, 5, tlist)

if __name__ == '__main__': 
    unittest.main()
