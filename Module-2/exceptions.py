def divide(num1, num2):
    return a/b


try:
     divide(10,0)

except:
    print("An error occurred during division.")

# we can also get the exeption type.
try:
    divide(10,0)
except Exception as e:
    print("exception type: ", type(e))

# we can also get the exception message.
try:
    divide(10,0)
except Exception: as e:
    print("exception message: ", e)

# We can also get exception class

try:
    divide(10,0)
except Exception as e:
    print("exception class: ", e.__class__)
