# Arguments and keyword arguments in Python functions.

# with args, you can pass in any amount of non -keyworded arguments to a function.

def add(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

result = add(2,3,4,5,6,7,8,10)

print("Sum using *args:", result)

# with kwargs, you can pass in any amount of keyworded arguments to a function.

def sum(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return sum

result = (sum(a=2, b=3, c=4, d=5))
print("Sum using **kwargs:", result)