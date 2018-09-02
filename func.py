def add(x, y):
	return x + y

def do_twice(func, x, y):
	return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b)) # output: 30

def add_five(x):
	return x + 5

def apply_twice(func, arg):
	return func(func(arg))

print(apply_twice(add_five, b)) # output: 20
