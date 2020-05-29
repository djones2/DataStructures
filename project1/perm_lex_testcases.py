import unittest
import perm_lex

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_empty(self):
        """ Test for empty string. """
        self.assertEqual(perm_lex.perm_gen_lex(''),[])
    
    def test_perm_gen_lex_single_char(self):
        """ Test for single character string. """
        self.assertEqual(perm_lex.perm_gen_lex('a'),['a'])
    
    def test_perm_gen_lex_two_char(self):
        """ Test for two character string. """
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab', 'ba'])

    def test_perm_gen_lex_many_char(self):
        """ Test for many character string. """
        self.assertEqual(perm_lex.perm_gen_lex('abc'),['abc', 'acb','bac', 'bca', 'cab', 'cba'])

if __name__ == "__main__":
        unittest.main()
