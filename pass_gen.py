import random

lower_case = 'abcdefghijklmnopqrstuwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUWZYZ'
number = '0123456789'
symbols = '!@#$%^&*+/\<>'

use = lower_case + upper_case + number + symbols

try:
    length_pass = int(input('Give me a length password: '))

    password = ''.join(random.sample(use, length_pass))

    print("\nYour generated password is: " + password)

except ValueError:
    print('ERROR value lenght !  Please give a number')
