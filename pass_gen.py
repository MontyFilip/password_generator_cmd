import random

lower_case='abcdefghijklmnopqrstuwxyz'
upper_case='ABCDEFGHIJKLMNOPQRSTUWZYZ'
number = '0123456789'
symbols='!@#$%^&*=+/\<>'

use = lower_case + upper_case + number + symbols

length_pass = 8

password = ''.join(random.sample(use, length_pass))

print("Your generated password is: " + password)