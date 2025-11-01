#Filtering a list

my_list = ["cappucino" , "expresso", "Americano", "capucano", "cortado"]

#function that filters my list and return only coffee that start with c
# Normal way
def find_coffee(list):
	new_list = []
	for coffee in list:
		if(coffee[0] == "c"):
			new_list.append(coffee)
	return new_list

# Using map
def find_coffee_function(coffee):
	if coffee[0] == 'c':
		return coffee

map_coffee = map(find_coffee_function, my_list)

for x in map_coffee:
	print(x)

# The map implementation above will print out all the list. for the coffee that doenst start with a 
#c, it will print it as none.

#Using the filter function. - The filter works just like the map, but in this case, 
# it will only return coffee that start with c. it will not print None

filter_coffee = filter(find_coffee_function, my_list)
for x in filter_coffee:
	print(x)