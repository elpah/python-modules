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


import json


 #User defined modules 
sys.path.insert(1, r'/Users/elpah/Desktop/python_modules/Final-Module/sample_to_import.py')
import sample_to_import

print(sample_to_import.names)
