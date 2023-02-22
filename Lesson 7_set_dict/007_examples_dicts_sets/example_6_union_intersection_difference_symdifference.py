A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Використання оператора |
# Виведення: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)

C = {1, 2, 3, 4, 5}
D = {4, 5, 6, 7, 8}
print(C.union(D))
print(D.union(C))
# /=====================/

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Використання оператора &
# Виведення: {4, 5}
print(A & B) #A.intersection(B)

# /=====================/

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Використання оператора - на A
# Виведення: {1, 2, 3}
print(A - B) # A.difference(B)
print(B - A) # B.difference(A)
print(A.difference(B))
print(B.difference(A))
set_1 = (A - B) | (B - A) # list of all unique elements from both lists
print(set_1)
set_2 = (A | B) - (A & B) # list of all unique elements from both lists
print(set_2)

# /=====================/

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Використання оператора ^
# Виведення: {1, 2, 3, 6, 7, 8}
print(A ^ B) # Symmetric Difference. list of all unique elements from both lists

# /=====================/

