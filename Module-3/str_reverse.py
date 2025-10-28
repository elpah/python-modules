# Reversing a string with a slice notation
#str[start:stop:step]

def reverse(s):
    return s[::-1]

#Another way using recursion

def reverse_str(str):
	if len(str) <= 1:
		return str
	return reverse_str(str[1:]) + str[0]

print(reverse_str("testing"))
print(reverse("Testing"))

