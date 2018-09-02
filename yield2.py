def get_even(x):
	for i in range(x):
		if i % 2 == 0:
			yield i

print(list(get_even(11)))