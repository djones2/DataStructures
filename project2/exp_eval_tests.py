# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    """
    def test_postfix_eval_01(self):
        self.assertEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)

    def test_postfix_eval_02(self):
        self.assertEqual(postfix_eval("10 1 >>"), 5)
 
    def test_postfix_eval_03(self):
        try:
            postfix_eval("blah")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("4 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_05(self):
        try:
            postfix_eval("1 2 3 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
    
    def test_postfix_eval_06(self):
        self.assertEqual(postfix_eval("10.2 2 +"), 12.2)

    def test_postfix_eval_07(self):
        try:
            postfix_eval("1.0 3 >>")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_08(self):
        self.assertAlmostEqual(12.0, postfix_eval("12.0"))

    def test_postfix_eval_09(self):
        self.assertAlmostEqual(12.1, postfix_eval("5 7.1 +"))
    
    def test_postfix_eval_10(self):
        self.assertAlmostEqual(-2.1, postfix_eval("5.1 -7.2 +"))

    def test_postfix_eval_11(self):
        with self.assertRaises(ValueError):  
            postfix_eval("12 1.2 * 10 10 - / 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 10 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual("3 4 - 5 +", infix_to_postfix("3 - 4 + 5"))
    """
    def test_infix_to_postfix_03(self):
        try:
            infix_to_postfix("( + ) )")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands") 

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")

if __name__ == "__main__":
    unittest.main()
