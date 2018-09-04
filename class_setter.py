class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings
		self._pineapple_allowed = False

	@staticmethod
	def validate_topping(topping):
		if topping == "pineapple":
			raise ValueError("No pineapples!")
		else:
			return True

	@property
	def pineapple_allowed(self):
		return self._pineapple_allowed

	@pineapple_allowed.setter
	def pineapple_allowed(self, value):
		if value:
			password = input("Enter the password: ")
			if password == "Sw0rdf1sh!":
				self._pineapple_allowed = value
			else:
				raise ValueError("Alert! Intruder!")
	

if __name__ == "__main__":
	ingredients = ["cheese", "onions", "tomato"]
	if all(Pizza.validate_topping(i) for i in ingredients):
		pizza = Pizza(ingredients)
	print(pizza.pineapple_allowed)
	pizza.pineapple_allowed = True
	print(pizza.pineapple_allowed)

