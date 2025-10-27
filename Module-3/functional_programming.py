#Two types of functions.
#1. Pure functions - these functions always return the same output for the same input and do not have any side effects.
#2. Impure functions - these functions may return different outputs for the same input or have



#Pure Functions
# doesn’t change or depend on anything outside its own scope (no modifying global variables, files, etc.).
# Given the same inputs, it always returns the same output no randomness, no side effects.
# A pure function should not manipulate or rely on data outside of its scope.

#example:
my_list = [1,2,3,4]

def append_to_list(lst, value):
    new_list = lst.copy()
    new_list.append(value)
    return new_list

#notice that my_list is not modified in the above function
print("Original list:", my_list)
new_list = append_to_list(my_list, 5)
print("New list after appending 5:", new_list)


#Impure Functions