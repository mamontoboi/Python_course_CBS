# example_3.py

class Bird:    
	TYPE = "Bird"

	def fly(self):        
		print(f"I am a {self.TYPE} and I can fly!")


class Horse:    
	TYPE = "Horse"

	def run(self):        
		print(f"I am a {self.TYPE} and I can run!")


class Pegas(Bird, Horse):
	pass


my_home_pegas = Pegas()
my_home_pegas.run()  # I am a Bird and I can run!
my_home_pegas.fly()  # I am a Bird and I can fly!  -- it inherits the TYPE from first parental class Bird
print(Pegas.__bases__)  # (<class '__main__.Bird'>, <class '__main__.Horse'>)
print(Pegas.__dict__)  # {'__module__': '__main__', '__doc__': None}
print(dir(my_home_pegas))  # ['TYPE', '__class__', '__delattr__', '__dict__', '__dir__', etc]
