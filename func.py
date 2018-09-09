def add(x, y):
	return x + y

def do_twice(func, x, y):
	return func(func(x, y), func(x, y))

def add_five(x):
	return x + 5

def apply_twice(func, arg):
	return func(func(arg))

# multi-arguments:
def multi_func(named_arg, *args):
	print(named_arg)
	print(args)

# default value:
def print_food(x, y, food="spam"):
	print(food)

# **kwargs:
def my_func(x, y=7, *args, **kwargs):
	print(kwargs)

def func_kwargs(**kwargs):
	print(kwargs["zero"])


if __name__ == '__main__':
	a = 5
	b = 10
	print(do_twice(add, a, b)) # output: 30
	print(apply_twice(add_five, b)) # output: 20
	multi_func(1, 2, 3, 4, 5)
	print_food(1, 2)
	print_food(3, 4, "egg")
	my_func(2, 3, 4, 5, 6, a=7, b=8)
	func_kwargs(a=0, zero=8)
