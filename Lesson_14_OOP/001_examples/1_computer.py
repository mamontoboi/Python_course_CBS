class BrowserWindow:
	def open(self, link):        
		self.current_link = link        
		print(f"Link '{link}' was opened!")


class Computer:
	def go_online(self):        
		return BrowserWindow()    

	def open_itvdn_lesson(self):        
		browser_window = self.go_online()        
		browser_window.open("itvdn.com")        

		return browser_window


my_own_computer = Computer()
browser = my_own_computer.open_itvdn_lesson()



# Use of context manager "with" for classes. Class needs to have _enter_ and _exit_ methods.
class Foo:
	def __enter__(self):
		return self

	def echo(self, x):
		print(x)

	def __exit__(self, exc_type, exc_val, exc_tb):
		return self


with Foo() as foo:
	foo.echo('123')