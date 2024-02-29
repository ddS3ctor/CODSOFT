'''
   Mpho Aphane                          -0~0-
   mpho4phane@gmail.com                  ._.       calculator/unittests.
'''

import unittest
from io import StringIO
from unittest.mock import patch
import task_2.calculator as calculator

class TestTask2(unittest.TestCase):
   @patch('sys.stdin', StringIO('2\n1 1\na a\n5\n99 3\n'))
   def test_get_number_input(self):
      expected_value = ['1', '1']
      return_value = calculator.get_number_input()
      self.assertTrue(isinstance(return_value, list))
      self.assertEqual(return_value, expected_value)
      
      expected_value = ['a', 'a']
      return_value = calculator.get_number_input()
      self.assertEqual(return_value, expected_value)
      
      expected_value = ['99', '3']
      return_value = calculator.get_number_input()
      self.assertEqual(return_value, expected_value)
      
   
   @patch('sys.stdin', StringIO('99 3\n'))   
   def test_validate_numbers(self):
      parameter = ['1', '1']
      expected_value = [1, 1]
      return_value = calculator.validate_numbers(parameter)
      self.assertEqual(return_value, expected_value)
      
      parameter = ['a', 'a']
      expected_value = [99, 3]
      return_value = calculator.validate_numbers(parameter)
      self.assertEqual(return_value, expected_value)
   
   
   @patch('sys.stdin', StringIO('+\n-\n/\n*\nWhatsApp\n+\n'))
   def test_expression_input(self):
      expected_value = '+'
      return_value = calculator.get_expression_input()
      self.assertEqual(return_value, expected_value)
      
      expected_value = '-'
      return_value = calculator.get_expression_input()
      self.assertEqual(return_value, expected_value)
      
      expected_value = '/'
      return_value = calculator.get_expression_input()
      self.assertEqual(return_value, expected_value)
      
      expected_value = '*'
      return_value = calculator.get_expression_input()
      self.assertEqual(return_value, expected_value)
      
      expected_value = '+'
      return_value = calculator.get_expression_input()
      self.assertEqual(return_value, expected_value)
      
      
   def test_calculate(self):
      numbers = [0, 2]
      expression = '+'
      expected_value = 2
      return_value = calculator.calculate(numbers, expression)
      self.assertEqual(return_value, expected_value)
      
      numbers = [5, 2]
      expression = '+'
      expected_value = 7
      return_value = calculator.calculate(numbers, expression)
      self.assertEqual(return_value, expected_value)
      
      numbers = [1, 1000]
      expression = '-'
      expected_value = -999
      return_value = calculator.calculate(numbers, expression)
      self.assertEqual(return_value, expected_value)
      
      numbers = [8, 7]
      expression = '-'
      expected_value = 1
      return_value = calculator.calculate(numbers, expression)
      self.assertEqual(return_value, expected_value)
      
      numbers = [4, 4]
      expression = '*'
      expected_value = 16
      return_value = calculator.calculate(numbers, expression)
      self.assertEqual(return_value, expected_value)
      
      numbers = [9999999, 0]
      expression = '*'
      expected_value = 0
      return_value = calculator.calculate(numbers, expression)
      self.assertEqual(return_value, expected_value)
      
      numbers = [9, 3]
      expression = '/'
      expected_value = 3
      return_value = calculator.calculate(numbers, expression)
      self.assertEqual(return_value, expected_value)
      
      numbers = [15, 2]
      expression = '/'
      expected_value = 7.5
      return_value = calculator.calculate(numbers, expression)
      self.assertEqual(return_value, expected_value)
      
      numbers = [32, 9]
      expression = '/'
      expected_value = 3.56
      return_value = calculator.calculate(numbers, expression)
      self.assertEqual(return_value, expected_value)
      
      
if __name__ == '__main__':
   unittest.main()