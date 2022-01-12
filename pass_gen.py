# natrixdev

# imports 
import random
import string 

# var
letters = string.ascii_letters

# script
password = input('Type something to create a pass/key:')
print('Here is your key  ')
print ( ''.join(random.choice(letters) for i in range(10)) )


# natrixdev
