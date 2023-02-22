class MyClass:
    my_attr = 1


m_c = MyClass()
m_c.my_attr = 54
print(hasattr(m_c, 'my_attr'))  # True
print(m_c.my_attr)  # 54
delattr(m_c, 'my_attr')
print(hasattr(m_c, 'my_attr'))  # True
print(m_c.my_attr)  # 1. Static attribute cannot be deleted if stated in class. Only changes, imposed by instance, can be deleted.
