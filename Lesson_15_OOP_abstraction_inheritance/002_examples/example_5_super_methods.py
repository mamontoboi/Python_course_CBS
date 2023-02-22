# example_5.py

class MathBase:
	def math_operation(self, number_1, number_2, operation):
		if operation == "-":            
			return number_1 - number_2        
		elif operation == "+":            
			return number_1 + number_2


class MathUpgrated(MathBase):    
	def math_operation(self, number_1, number_2, operation):
		# if the operation refers to method, described in parental class, it can be forwarded to it and asked for results
		if operation in ["+", "-"]:
			parent_class_object = super()
			result = parent_class_object.math_operation(number_1, number_2, operation)
			return result        
		elif operation == "*":            
			return number_1 * number_2        
		elif operation == "/":            
			return number_1 / number_2        


my_math = MathUpgrated()

print(my_math.math_operation(4, 2, "+"))  # ==> 6 -- rcvs answer from parental class

print(my_math.math_operation(4, 2, "-"))  # ==> 2 -- rcvs answer from parental class

print(my_math.math_operation(4, 2, "/"))  # ==> 2.0 -- rcvs answer from its own method

print(my_math.math_operation(4, 2, "*"))  # ==> 8  -- rcvs answer from its own method
