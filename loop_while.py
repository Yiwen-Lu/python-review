i = 0

while True:
	i += 1
	if i == 2:
		print('Skipping 2')
		continue
	elif i == 5:
		print('Breaking')
		break
	print(i)

print('Finished!')