# Dictionary Data Structure Examples

sample_dict = {1:"apple", 2:"banana", 3:"cherry"}

mixed_dict = {"integer":1, "float":5.22, "bool":True, "string":"hello"}

# to print an item in a dictionary, we can use the key inside square brackets or the get method
print("printing item with key 1: ", sample_dict[1])
print("printing item with key float: ", mixed_dict["float"])

print("printing item with key 'string': ", mixed_dict.get("string"))

#we can also change the value of an item in a dictionary by specifying th ekey and assigning a new value.
mixed_dict["integer"] = 583
print("After changing value of key 'integer': ", mixed_dict)


#To iterate through a dictionary we can use for loop to get both keys and values using the items() method

for key,value in sample_dict.items():
    print("key:value.", key,":", value)