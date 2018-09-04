class Queue:
	def __init__(self, contents):
		self._hiddenlist = contents

	def push(self, value):
		return self._hiddenlist.insert(0, value)

	def pop(self):
		return self._hiddenlist.pop(-1)

	def __repr__(self):
		return "Queue({})".format(self._hiddenlist)


class Egg:
	__egg = 7
	def print_egg(self):
		print(self.__egg)


if __name__ == "__main__":
	queue = Queue([1, 2, 3])
	print(queue)
	queue.push(0)
	print(queue)
	queue.pop()
	print(queue)
	print(queue._hiddenlist)

	egg = Egg()
	egg.print_egg()
	print(egg._Egg__egg)
	#print(egg.__egg) # AttributeError here
	"""strongly private (begins with __) methods and attributes 
	can't be accessed from outside the class"""