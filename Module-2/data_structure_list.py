list1 = [1,2,3,4,5]
list2 = ["text1", "text2", "text3"]
list3 = [1, "text", 3.14, True]


# to print a list
print(*list1)

#print with separator
print(*list1, sep=",")

#or with the array brackets and a separator / no unpacking
print(list1, sep=",")

# to add items to a list

# to add a single item
list1.append(6)
print("After appending 6:", list1)


# to add multiple items
list1.extend([8,9,10,11])
print("After extending with [8,9,10,11]:", list1)

#to add a an item at a specific index, we can use insert
list1.insert(0,0) #inserts 0 at index 0
print("After inserting 0 at index 0:", list1)  

list2.insert(1,"inserted_text") #inserts "inserted_text" at index 1
print("After inserting 'inserted_text' at index 1:", list2)

# to remove an item, we can use pop and specify the index, or remove and specify the value;

list1.pop(len(list1)-1) #removes last item
print("After popping last item:", list1)

list1.remove(3) #removes first occurrence of value 3
print("After removing value 3:", list1)

# we can also remove item from the list using del keywod and specifying the index
del list1[0] #removes first item
print("After deleting first item:", list1)

#we can also iterate through a list using a for loop
for item in list2:
    print("List2 item:", item)
