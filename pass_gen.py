import random

def generate_password():
    lower_case = 'abcdefghijklmnopqrstuwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUWZYZ'
    number = '0123456789'
    symbols = '!@#$%^&*+/\\<>'
    
    use = lower_case + upper_case + number + symbols


    try:
        length_pass = int(input('Give me a length for the password (minimum 8 characters): '))
        if length_pass < 8:
            print('ERROR: Password length must be at least 8 characters.')
        else:
            password = ''.join(random.sample(use, length_pass))
            return password
    except ValueError:
        print('ERROR: Invalid length! Please provide a valid number.')

try:
    print("\nYour generated password is:", generate_password())

except KeyboardInterrupt:
    print("\n\nPassword generation interrupted by user.")
