# Algorithms is a series of step-by-step instructions to solve aproblem of perform a task.
# Real life example
# Example: Checking if a string is a palindrome 

def isPalindrom(string):                           
    endIndex = len(string) - 1                      
    start_index = 0                                 
    while start_index < endIndex:                   
        if string[start_index] != string[endIndex]: 
            return False     
        start_index += 1
        endIndex -= 1
    return True
    
print(isPalindrom("racecar"))
print(isPalindrom("hello"))

#Recursion - a method of solving problem where a function will call itself until a base condition is met.
def factorial(n):
    if n = 0:
        return 1
    else:
        return (n * factorial(n-1))
        