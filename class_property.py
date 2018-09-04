class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings

	@staticmethod
	def validate_topping(topping):
		if topping == "pineapple":
			raise ValueError("No pineapples!")
		else:
			return True

	@property
	def pineapple_allowed(self):
		return False
	

if __name__ == "__main__":
	ingredients = ["cheese", "onions", "tomato"]
	if all(Pizza.validate_topping(i) for i in ingredients):
		pizza = Pizza(ingredients)
	print(pizza.pineapple_allowed)

