def polynomial(x):
	return x**2 + x*5 + 4

print(polynomial(-4))
print((lambda x: x**2 + x*5 + 4) (-4)) # no comma ","