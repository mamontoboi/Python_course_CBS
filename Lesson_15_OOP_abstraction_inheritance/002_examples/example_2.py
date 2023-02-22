# example_2.py

class Cat:    
	def __init__(self, name):        
		self.name = name    

	def say_meow(self):        
		print(f"{self.name}: Meow!")


class UpdateCat(Cat):
	def bite_a_finger(self):        
		print("Bite! :)")
		

my_cat = Cat("Black")
my_kitty = UpdateCat("Gray")

my_cat.say_meow()
my_kitty.say_meow()
my_kitty.bite_a_finger()
