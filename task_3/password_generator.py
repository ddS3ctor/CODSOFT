'''
   Mpho Aphane                           0 0
   mpho4phane@gmail.com                  ._.
'''


from random import randint as shuffle

def get_password_length():
    '''Promp the user for the length of the password.
    
       Returns the length as String
    '''
    return input('Insert the length of your password (from 4 to 20): ')


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


def generate_password(length: int):
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
    
    gen_2_letters = letters[shuffle(0, len(letters) - 1)].upper() + letters[shuffle(0, len(letters) - 1)]
    password.append(gen_2_letters[0])
    password.append(gen_2_letters[1])
    password.append(numbers[shuffle(0, len(numbers) - 1)])
    password.append(special_chars[shuffle(0, len(special_chars) - 1)])
    
    if length > 4:
        all_keys = special_chars + numbers + letters + [convert_to_upper.upper() for convert_to_upper in letters]
        for i in range(length - 4): password.append(all_keys[shuffle(0, len(all_keys) - 1)])
    
    for i in range(len(password)):
        shuffle_index = shuffle(0, len(password) - 1)
        while shuffle_index == i: shuffle_index = shuffle(0, len(password) - 1)
        value_index = password[i]
        password[i] = password[shuffle_index]
        password[shuffle_index] = value_index
        
    return ''.join(password)


def start_program():
    '''Main function.'''
    length = get_password_length()
    password = generate_password(validate_length(length))
    print(password)


if __name__ == '__main__':
    start_program()