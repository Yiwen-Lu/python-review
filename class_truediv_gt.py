class SpecialString:
	def __init__(self, cont):
		self.cont = cont

	def __truediv__(self, other):
		line = "=" * len(self.cont)
		return "\n".join([self.cont, line, other.cont])

	def __gt__(self, other):
		for idx in range(len(other.cont) + 1):
			result = other.cont[:idx] + ">" + self.cont
			result += ">" + other.cont[idx:]
			print(result)


if __name__ == '__main__':
	spam = SpecialString("spam")
	hello = SpecialString("Hello World!")
	eggs = SpecialString("eggs")
	print(spam / hello)
	spam > eggs # no need of print