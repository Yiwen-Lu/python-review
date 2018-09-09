try:
	print(1)
except ZeroDivisionError:
	print(2)
else:
	print(3)

try:
	print(1/0)
except ZeroDivisionError:
	print(4)
else:
	print(5)

"""
output:
1
3
4
"""

try:
	print(1)
	print(1 + "1" == 2)
	print(2)
except TypeError:
	print(3)
else:
	print(4)

"""
output:
1
3
"""

for i in range(10):
	try:
		if 10 / i == 2.0:
			break
	except:
		print(1)
	else:
		print(2)

"""
output:
1
2
2
2
2
"""

