# Modules - Building blocks for adding functionality in your code withou having 
# to rewrite those functions/blocks
#can contain both executable statemnts and functions

#Types
 #Builtin Modules - eg: sys , math

import sys
location = sys.path
for i in location:
    print(i)

import calendar
leapdays = calendar.leapdays(2000, 2050)
print(leapdays)

is_it_leap = calendar.isleap(2024)
print(is_it_leap)

#User defined modules 
# sys.path.insert(1, r'/Users/elpah/Desktop/python_modules/Final-Module/sample_to_import.py') - add the directory path if you are importing from another directory
import sample_to_import

print(sample_to_import.names)

#instead of importing the whole math module, we can specifically import what we need. 
#example
# import math
# import math as variable_name - exampl: import math as m
# we can also import multiple functions that we need from math. example : from math import sqrt, factorial, log10


from math import sqrt
print("importing maths module")
# sqroot = math.sqrt(25)
sqroot = sqrt(25)
print(sqroot)


