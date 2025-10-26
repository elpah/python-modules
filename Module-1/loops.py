#For Loops
# example looping through a string

string_name = "Testing Loop"

for item in string_name:
	print(item)

#looping numbers 0 to 10
for i in range(10):
	print("looping..", i)

#Looping through an Array

names = ["Kofi", "Ama", "James", "John", "Elpah"]

for name in names:
	print(name)


#While Loop
num = 0
while num < 20:
	print(num)
	num += 1

count = 0
while count < len(names):
	print(names[count])
	count +=1
