# TypeCasting - converting data from one data type to another

# --------------------------
# Implicit Type Casting
# --------------------------
# Performed automatically by Python when two compatible types are used together

a = 5       # int
b = 2.5     # float

c = a + b   # int + float => float
print(c)    # Output: 7.5
print(type(c))  # <class 'float'>

# --------------------------
# Explicit Type Casting
# --------------------------
# Performed manually by the developer using functions like str(), int(), float(), etc.

# Converting to string
x = str(11)
print(x, type(x))  # Output: '11' <class 'str'>

# Converting to int
y = int("11")
print(y, type(y))  # Output: 11 <class 'int'>

# Converting to float
z = float("11.4")
print(z, type(z))  # Output: 11.4 <class 'float'>

# Converting to hexadecimal
h = hex(10)
print(h, type(h))  # Output: '0xa' <class 'str'>

# Converting to octal
o = oct(10)
print(o, type(o))  # Output: '0o12' <class 'str'>

# Converting to tuple
t = tuple([1, 2, 3])
print(t, type(t))  # Output: (1, 2, 3) <class 'tuple'>

# Converting to set
s = set([1, 2, 2, 3])
print(s, type(s))  # Output: {1, 2, 3} <class 'set'>

# Converting to list
l = list((1, 2, 3))
print(l, type(l))  # Output: [1, 2, 3] <class 'list'>

# Converting to dictionary
# Needs key-value pairs (like a list of tuples)
d = dict([('a', 1), ('b', 2)])
print(d, type(d))  # Output: {'a': 1, 'b': 2} <class 'dict'>

# Converting a character to its Unicode integer value
char_val = 'A'
num_val = ord(char_val)
print(num_val, type(num_val))  # Output: 65 <class 'int'>

# Converting an integer to a character
char_from_num = chr(65)
print(char_from_num, type(char_from_num))  # Output: 'A' <class 'str'>
