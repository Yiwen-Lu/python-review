class A:
	def a(self):
		print(1)

	def method(self):
		print("A method")


class B(A):
	def a(self):
		print(2)

	def another_method(self):
		print("B method")


class C(B):
	def c(self):
		print(3)

	def third_method(self):
		print("C method")


class D(A):
	def a(self):
		print(2)
		super().a()
		

if __name__ == '__main__':
	c = C()
	c.method()
	c.another_method()
	c.third_method()
	c.a() # 2
	D().a()