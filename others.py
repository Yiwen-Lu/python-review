# truple unpacking:
nums = (1, 2, 3)
a, b, c = nums

print(a)
print(b)
print(c)


nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
a, b, *c, d = nums

print(a)
print(b)
print(c)
print(d)

# Ternary Operator:
a = 7
b = 1 if a >= 5 else 42

print(b)


status = 1
msg = "Logout" if status == 1 else "Login"

print(msg)


# for loop - break - attention to 'else' position!!!:
for i in range(10):
	if i == 999:
		break
else:
	print("Unbroken 1")

for i in range(10):
	if i == 5:
		break
else:
	print("Unbroken 2")

for i in range(10):
	if i > 5:
		print(i)
		break
else:
	print("7")

	