import heapq
"""Module is used to make changes to the list"""

li = [2, 4, 1, 3, 8]

heapq.heapify(li) # create heap

heapq.heappush(li, 5)  # [1, 3, 2, 4, 8, 5] -- adds item to the list
print(li)

i = heapq.heappop(li)  # removes the smallest item from the list
print(li)  # [2, 3, 5, 4, 8]
print(i)  # 1

print(heapq.nlargest(3, li))  # [8, 5, 4] -- 3 largest items in the list

print(heapq.nsmallest(3, li))  # [2, 3, 4] -- 3 smallest items in the list

print(heapq.heappushpop(li, 7))  # 2 -- returns the smallest value and insert value in parentheses into the list
print(heapq.heappushpop(li, 9))  # 3 -- same. First push, than smallest popped.
print(li)  # [4, 7, 5, 9, 8]

heapq.heapreplace(li, 25)  # first smallest element is popped, then value in parentheses is inserted.
print(li)  #[5, 7, 25, 9, 8]



