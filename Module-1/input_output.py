#we can use the input function to collect data from a user. 
name = input("Please enter your name:")
age =  input("Please enter your age:")
city =  input("Please enter your city name:")
text = f"Your name is {name}. You are {age} years old. You live in {city}."
print(text)

# We can use the print() function to display data on the screen.
# It can print all data types, arithmetic values, etc.

# Take input from the user
num1 = input("Please enter first number: ")
num2 = input("Please enter second number: ")

# Input from input() is always a string, so convert to int
num1 = int(num1)
num2 = int(num2)

print("The sum of num1 and num2 is: ", num1+num2)
print("We can also print a float value like this: ",200.928)
print("The sum of num1 and num2 is: ",num1*num2)
