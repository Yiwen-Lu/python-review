class Cat:
	def __init__(self, color, legs):
		self.color = color
		self.legs = legs

class Dog:
	legs = 4
	def __init__(self, name, color):
		self.name = name
		self.color = color
	
	def bark(self):
		print("Woof!")

class Student:
	def __init__(self, name):
		self.name = name

	def sayHi(self):
		print("Hi from" + self.name)


if __name__ == '__main__':
	kitty = Cat("pink", 4)
	print(kitty.color, kitty.legs)

	snoopy = Dog("Snoopy", "white")
	print(snoopy.name, snoopy.color)
	snoopy.bark()
	print(snoopy.legs, Dog.legs)

	s1 = Student("Amy")
	s1.sayHi()