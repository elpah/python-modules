# class Recipe:
# 	def __new__(cls):
# 		pass
# 	def __init__(self):
# 		pass



class Recipe:
	def __init__(self,dish,items,time):
		self.dish = dish
		self.items = items
		self.time = time
	
	def content(self):
		print("The ",self.dish , " has ", self.items, " and takes " , str(self.time),  " to prepare\n")


pizza = Recipe('Pizza',["cheese", "bread", "tomatoes"], 45)
pasta = Recipe('Pasta',["cheese", "penne", "tomatoes"], 55)

print(pizza.content())
print(pasta.content())

