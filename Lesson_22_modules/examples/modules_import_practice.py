"""So...
1) In order to create package folder it is necessary to add __init__.py into a folder. 

2) After this it is necessary to import various modules, stored inside the folder, into the __init__ file.
'from .my_module1 import *
from .my_module2 import *
or 
from . import my_module1, my_module2

3) Create variable __all__ that allows modules to be visible from outside
#__all__ = ['my_module1', 'my_module2']'

4) In modules themselves make 
__all__ = ['a']
to give outside access to variable a.

5) Operate in the following manner: 
"""

import my_package.my_module1
from my_package import a
from my_package import h

my_package.my_module1.a = 5
my_package.my_module1.my_average()
print(my_package.h)
