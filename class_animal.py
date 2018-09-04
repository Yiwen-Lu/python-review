class Animal:
	def __init__(self, name, color):
		self.name = name
		self.color = color

class Cat(Animal):
	def purr(self):
		print("Purr...")


class Wolf:
	def __init__(self, name, color):
		self.name = name
		self.color = color
	def bark(self):
		print("Grr...")

class Dog(Wolf):
	def bark(self):
		print("Woof!")


if __name__ == '__main__':
	kitty = Cat("Kitty", "pink")
	print(kitty.name)

	snoopy = Dog("Snoopy", "white")
	print(snoopy.name)
	snoopy.bark()