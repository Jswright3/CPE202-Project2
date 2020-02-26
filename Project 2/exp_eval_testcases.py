"""
CPE202
Project 2
John Wright
"""
import unittest
from exp_eval import *

class MyTest(unittest.TestCase):

   def test_infix_to_postfix(self):
      self.assertEqual(infix_to_postfix('2 + 3 * 4'), '2 3 4 * +')
      self.assertEqual(infix_to_postfix('( 1 + 2 ) * 7'), '1 2 + 7 *')
      self.assertEqual(infix_to_postfix('( 1 / ( 2 - 3 + 4 ) ) * ( 5 - 6 ) * 7'), '1 2 3 - 4 + / 5 6 - * 7 *')
      #self.assertRaises(SyntaxError, infix_to_postfix, '3 0')

      # Test Cases from Sample
      self.assertEqual(infix_to_postfix('( ( 5 - 3 ) ^ 2 + ( 4 - 2 ) ^ 2 ) ^ ( 1 / 2 )'),'5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^')
      self.assertEqual(infix_to_postfix('5 * 3 ^ ( 4 - 2 )'),'5 3 4 2 - ^ *')
      self.assertEqual(infix_to_postfix('( ( 1 * 2 ) + ( 3 / 4 ) )'),'1 2 * 3 4 / +')
      self.assertEqual(infix_to_postfix('( ( 2 * ( 3 + 4 ) ) / 5 )'),'2 3 4 + * 5 /')
      self.assertEqual(infix_to_postfix('( 3 * ( 4 + 6 / 3 ) )'),'3 4 6 3 / + *')
      self.assertEqual(infix_to_postfix('( ~ 3 ) ^ 2 + 9'),'3 ~ 2 ^ 9 +')
      self.assertEqual(infix_to_postfix('~ 3 ^ 2 + 9'),'3 2 ^ ~ 9 +')
      self.assertEqual(infix_to_postfix('4 ^ ( ~ 1 ) * 4'),'4 1 ~ ^ 4 *')
      self.assertEqual(infix_to_postfix('~ 1'),'1 ~')
      self.assertEqual(infix_to_postfix('1'), '1')

      #Having Trouble with case where there is a two digit number, and where to place the negative sign
      #self.assertEqual(infix_to_postfix('10 + 3 * 5 / ( 16 - 4 )'), '10 3 5 16 4 - / * +')
      #self.assertEqual(infix_to_postfix('~ 3 * 3 + 9'),'3 ~ 3 * 9 +')
      #self.assertEqual(infix_to_postfix('~ ~ 1'),'1 ~ ~')


   def test_postfix_eval(self):
      self.assertEqual(postfix_eval('1 2 7 * +'), 15)
      self.assertAlmostEqual(postfix_eval('1 2 3 - 4 + / 5 6 - * 7 *'), -2.3333333)
      self.assertEqual(postfix_eval('2 3 4 * + ~'), -14)
      self.assertEqual(postfix_eval('3 2 ^'), 9)
      self.assertEqual(postfix_eval('9 3 /'), 3)
      self.assertEqual(postfix_eval('9 3 -'), 6)
      self.assertRaises(ZeroDivisionError, postfix_eval, '3 0 /')
      self.assertRaises(SyntaxError, postfix_eval, '~ 3 ^ 2')

   def test_postfix_valid(self):
      self.assertTrue(postfix_valid('3 5 +'))
      self.assertTrue(postfix_valid('1 2 + 7 *'))
      self.assertTrue(postfix_valid('1 2 3 - 4 + / 5 6 - * 7 *'))
      self.assertTrue(postfix_valid('3 2 ^ ~'))

if __name__ == '__main__':
    unittest.main()

