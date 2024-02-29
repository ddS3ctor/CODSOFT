'''
   Mpho Aphane                          -0~0-
   mpho4phane@gmail.com                  ._.
'''

import unittest
from io import StringIO
from unittest.mock import patch
import task_3.password_generator as password_generator

class TestTask3(unittest.TestCase):
    
    # Testing the get_password_length function which prompts the user to input the length of the password
    # by mocking the input using patch when calling the function, the return
    # value must be the same as the input value of String type.
    @patch('sys.stdin', StringIO('Mpho\n9\n1 up\ntail\nCool\nJuiCe\n'))
    def test_get_password_length(self):
        return_value = password_generator.get_password_length()
        self.assertTrue(isinstance(return_value, str))
        self.assertEqual(return_value, 'Mpho')
        
        return_value = password_generator.get_password_length()
        self.assertTrue(isinstance(return_value, str))
        self.assertEqual(return_value, '9')
        
        return_value = password_generator.get_password_length()
        self.assertTrue(isinstance(return_value, str))
        self.assertEqual(return_value, '1 up')
        
    
    # The validate_length function calls the get_input function if an invalid input was provided.
    # This annotation serves to mock valid input after testing the validate_length function with an invalid input.
    @patch('sys.stdin', StringIO('9\n16\n'))
    def test_validate_length(self):
        # Test the validate_length function with an invalid password length of '1' which is not in the required range.
        return_value = password_generator.validate_length('1')
        
        # The patch annotation provides a valid password length of 9 which gets returned as an integer.
        self.assertTrue(isinstance(return_value, int))
        self.assertEqual(return_value, 9)
        
        
        # Test the validate_length function with an invalid password length of 'Python'.
        return_value = password_generator.validate_length('Python')
        
        # The patch annotation provides a valid password length of 16 which gets returned as an integer.
        self.assertTrue(isinstance(return_value, int))
        self.assertEqual(return_value, 16)
        
        
        # Test the validate_length function with a valid password length of '20' which should be returned as an int
        # Mocking is not required since the value of the parameter is in range.
        return_value = password_generator.validate_length('20')
        self.assertTrue(isinstance(return_value, int))
    
    
    def test_generate_password(self):
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', 
                     '_', '=', '+', '\\', '/', ',', '.', '?', '<', '>', '`',
                    '~', '[', ']', '{', '}', '"', '\'']
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        # Test whether the generated password has a small-case and upper-case letter.
        result = password_generator.generate_password(9, '1') # Complexity of 1: Low
        self.assertTrue([result_char in letters for result_char in result], 
                        'Check if the password has a lower-case letter.')
        self.assertTrue(
[result_char in [convert_to_upper.upper() for convert_to_upper in letters] for result_char in result], 
                        'Check if the password has a upper-case letter.')
        self.assertTrue([result_char in letters for result_char in result])
        
        
        # Test whether the generated password has a small-case and upper-case letter and a number.
        result = password_generator.generate_password(16, '2') # Complexity of 2: MEDIUM
        self.assertTrue([result_char in letters for result_char in result], 
                        'Check if the password has a lower-case letter.')
        self.assertTrue(
[result_char in [convert_to_upper.upper() for convert_to_upper in letters] for result_char in result], 
                        'Check if the password has a upper-case letter.')
        self.assertTrue([result_char in numbers for result_char in numbers], 
                        'Check if the password has a number.')
        
        
        # Test whether the generated password has a small-case and upper-case letter and a number.
        result = password_generator.generate_password(16, '3') # Complexity of 1: HIGH
        self.assertTrue([result_char in letters for result_char in result], 
                        'Check if the password has a lower-case letter.')
        self.assertTrue(
[result_char in [convert_to_upper.upper() for convert_to_upper in letters] for result_char in result], 
                        'Check if the password has a upper-case letter.')
        self.assertTrue([result_char in numbers for result_char in numbers], 
                        'Check if the password has a number.')
        self.assertTrue([result_char in special_chars for result_char in special_chars], 
                        'Check if the password has a special character.')
        
    
if __name__ == '__main__':
    unittest.main()