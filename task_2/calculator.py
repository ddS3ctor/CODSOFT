'''
   Mpho Aphane                           0 0
   mpho4phane@gmail.com                  ._.       calculator.
'''

DARK_GRAY = "\033[1;30m"
BOLD = "\033[1m"
END = '\033[0m'


def get_number_input():
   '''Prompt the user to input two numbers.
      Return value: a list with two numbers
   '''   
   numbers = []
   while len(numbers) != 2:
      numbers = input('Insert two numbers (separated by blank-space. e.g. 80 199): ').split()
      if numbers[0] == 'quit':
         exit()
      elif len(numbers) != 2: print('Two numbers required!')
   return numbers


def validate_numbers(numbers: list):
   '''Validate the argument of the list parameter by checking if the values contain only integers.
      Print an error message if a value is invalid and call the get_numbers to reprompt, 
      otherwise return parameter.
   '''
   for i in range(0, len(numbers)):
      try: 
         x = int(numbers[i])
         numbers[i] = x
      except:
         i = 0
         print('Invalid value: ' + str(numbers[i]))
         numbers = get_number_input()
         validate_numbers(numbers)
         
   return numbers


def get_expression_input():
   '''Prompt the user to input a valid arithmetic expression and return it.'''
   
   expressions = ['+', '-', '*', '/']
   expression = input('Insert an arithmatic expression to perform a calculation: ')
   
   while expression not in expressions:
      expression = input('Insert an arithmatic expression to perform a calculation: ')
   return expression


def calculate(numbers: list, expression):
   '''Perform the calculation and return the result.'''
   x = numbers[0]
   y = numbers[1]
   result = 0
   
   if expression == '+': result = x + y
   elif expression == '-': result = x - y
   elif expression == '*': result = x * y
   elif expression == '/':
      if expression == '/' and y == 0:
         print('Error: Division by zero is undefined!')
         result = calculate(validate_numbers(get_number_input()), expression)
      else: result = x / y
      if x % y != 0: result = round(result, 2)
   
   return result


if __name__ == '__main__':
   history = []
   developer = 'Mpho Aphane'
   print(' '*38 + BOLD + 'SIMPLE' + END)
   print(' _____     __    __       _____  ___  __ __         __  _______  _____   _____   ')
   print('[|    |    /\    [|      [|    | | |   | [|         /\  \  |  / |   |||  [|   [| ')
   print('[|        /__\   [|      [|      ||    | [|        /__\    |    |    ||  [|   /  ')
   print('[|____| _/    \_ [|____| [|____| |_____| [|____| _/    \_ _|_   |_____| _[|_  \. ')
   print(' '*36 + DARK_GRAY + developer + END)
   
   numbers = get_number_input()
   numbers = validate_numbers(numbers)
   expression = get_expression_input()
   answer = (calculate(numbers, expression))
   print('Answer = ' + str(answer))
   history.append(answer)