new_tuple = (1,True, 3.4, "hello")


# to print the tuple
print("Tuple contents:", new_tuple)

#to print a specific item in the tuple, we can use indexing
print("First item in tuple:", new_tuple[0])

# to print type of item in the tuple
print("Type of second item in tuple:", type(new_tuple[1]))


#we can also declare a tuple without parentheses
another_tuple = 2, False, 5.6, "world"
print("Another tuple contents:", another_tuple) 


#tuples are immutable, so we cannot add or remove items from a tuple
#the following lines would raise an error if uncommented
#new_tuple.append(5)
#new_tuple.remove(1)

# we can count the number of times an item appears in a tuple using the count method.

print("count number of 1s in a tuple: ", new_tuple.count(1))
 #funny enough this line prints 2 since True is considered as 1 in python.


#  we can also get the index of where an item appears in a tuple using the index method.

print("index of hello in tuple is: ", new_tuple.index("hello"))

# we can also loop through a tuple using a for loop.

for item in new_tuple:
    print("Tuple item:", item)