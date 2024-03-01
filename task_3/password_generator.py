'''
   Mpho Aphane                           0 0
   mpho4phane@gmail.com                  ._.       password_generator.
'''


from random import randint as shuffle

LIGHT_BLUE = '\033[1;34m'
YELLOW = '\033[1;33m'
GREEN = '\033[0;32m'
END = '\033[0m'


def get_password_length():
    '''Promp the user for the length of the password.
    
       Returns the length as String
    '''
    return input('Insert the length of your password (from 4 to 20): ')


def get_complexity_input():
    '''Prompt the user for the complexity of the password (1: LOW, 2:MEDIUM or 3: HIGH)'''
    
    prompt_msg = \
    'Choose the complexity of your password: \n  ' + YELLOW + '1' + END + ': LOW\n  ' + \
    LIGHT_BLUE + '2' + END + ': MEDIUM\n  ' + GREEN + '3' + END +': HIGH' + '\n'
    complexity = input(prompt_msg)
    complexity_range = ['1', '2', '3']
    while complexity not in complexity_range:
        print('Invalid complexity')
        complexity = input(prompt_msg)
        
    return complexity


def validate_length(length):
    '''Check the value of the length parameter if it is a positive integer 
       ranging from 4 to 20, violation of these constraints calls the 
       get_password_length() function.
       
       Returns the length as an Integer
    '''
    while isinstance(length, str):
        try:
            length = int(length)
            if length < 4 or length > 20:
                print('Invalid range!')
                length = get_password_length()
        except:
            print('Invalid input! Insert a positive integer.')
            length = get_password_length()
            
    return length


def generate_password(length: int, complexity):
    '''Algorithm for generating a secured password, containing at least 
       upper-case & lower-case letter(s), numerical-value(s) and 
       special-character(s).
       
       Returns a String of the generated password
    '''
    password = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', 
                     '_', '=', '+', '\\', '/', ',', '.', '?', '<', '>', '`',
                    '~', '[', ']', '{', '}', '"', '\'']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    all_chars = special_chars + numbers + letters + [convert_to_upper.upper() for convert_to_upper in letters]
    # password_base_case is a generated password containg 4 values in this order:
    # (1-lower case letter), (2-uppercase letter), (3-number) and (4-special character)
    password_base_case = letters[shuffle(0, len(letters) - 1)].upper() + letters[shuffle(0, len(letters) - 1)] \
        + numbers[shuffle(0, len(numbers) - 1)] + special_chars[shuffle(0, len(special_chars) - 1)]
    
    # Append these 4 values to the password list
    for char in password_base_case: password.append(char)
    
    # Complexity of 3 will generate a password with a lower and upper case letter,
    # a number and a special character.
    if complexity == '3':
        if length > 4:
            for i in range(length - 4): password.append(all_chars[shuffle(0, len(all_chars) - 1)])
    # Complexity of 2 will generate a password with a lower and upper case letter and a number.
    elif complexity == '2':
        gen_2_numbers = numbers[shuffle(0, len(numbers) - 1)] + numbers[shuffle(0, len(numbers) - 1)]
        password[2] = gen_2_numbers[0]
        password[3] = gen_2_numbers[1]
        if length > 4:
            numbers_and_letters = letters + numbers + [letter for letter in letters]
            for i in range(length - 4): 
                password.append(numbers_and_letters[shuffle(0, len(numbers_and_letters) - 1)])
    # The else statement evaluates to a Complexity of 1 which will generate a password that has
    # at least 1 upper case and 1 lowercase.
    else:
        gen_2_letters = letters[shuffle(0, len(letters) - 1)].upper() + letters[shuffle(0, len(letters) - 1)]
        password[2] = gen_2_letters[0]
        password[3] = gen_2_letters[1]
        if length > 4:
            upper_and_low_case_letters = letters + [letter.upper() for letter in letters]
            for i in range(length - 4): 
                password.append(upper_and_low_case_letters[(shuffle(0, len(upper_and_low_case_letters) - 1))])
    
    # Shuffle the positions of the generated password.
    for i in range(len(password)):
        shuffle_index = shuffle(0, len(password) - 1)
        while shuffle_index == i: shuffle_index = shuffle(0, len(password) - 1)
        value_index = password[i]
        password[i] = password[shuffle_index]
        password[shuffle_index] = value_index
        
    return ''.join(password)


def start_program():
    '''This function orchestrates the procedure of generating a password.'''
    length = get_password_length()
    complexity = get_complexity_input()
    password_msg = 'Password Generated Successfully: '
    password = generate_password(validate_length(length), complexity)
    
    if complexity == '1': print(YELLOW + password_msg + END + password)
    elif complexity == '2': print(LIGHT_BLUE + password_msg + END + password)
    else: print(GREEN + password_msg + END + password)


if __name__ == '__main__':
    start_program()