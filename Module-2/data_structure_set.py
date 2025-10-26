set_a = {1,2,3,4,5}
set_b = {"apple", "banana", "cherry" ,1,2,5,8,9}
set_c = {1, "text", 3.14, True}

#unlike lists, sets do not allow duplicate values. while it may not complain if we try to add a duplicate value, it will simply ignore it.
#also set do not have indexes like lists or tuples. the items in a set are unordered and cannot be accessed using an index.
#sets also have methods.
# to add an item to a set, we can use the add method.

set_a.add(6)
print("After adding 6:", set_a)

set_a.remove(2) #removes 2 from the set.  
print("After removing 2:", set_a)

#we can also use discard to remove an item. the difference is that discard will not raise an error if the item is not found in the set.
set_a.discard(10) #does not raise an error
print("After discarding 10 (not in set):", set_a)

#Union Set - we can join two sets using the union method or the | operator.
set_d = set_a.union(set_b)
print("Union of set_a and set_b using union method:", set_d)

set_e = set_a | set_b
print("Union of set_a and set_b using | operator:", set_e)


# Intersect Set - we can use the intersection method or & operatior to get the common items in two sets.
set_f = set_a.intersection(set_c)
print("Intersection of set_a and set_c using intersection method:", set_f)

setf = set_a & set_c
print("Intersection of set_a and set_c using & operator:", setf)


# Difference Set. we can use the difference method or - operator, to get items in one set that are not in the other set.

set_g = set_a.difference(set_b)
print("Difference of set_a and set_b using difference method:", set_g)

set_h = set_a - set_b
print("Difference of set_a and set_b using - operator:", set_h)

#Symmetric DIfference Set - we can use the symmetric_difference method or ^ operator to get all elements that are ni either of the sets but not in both.

set_i = set_a.symmetric_difference(set_b)
print("Symmetric difference of set_a and set_b using symmetric_difference method:", set_i)

set_j = set_a ^ set_b
print("Symmetric difference of set_a and set_b using ^ operator:", set_j)