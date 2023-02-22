# Є два списки, які наповнюються користувачем з клавіатури. Сформувати список, в якому будуть міститися
# унікальні значення першого відносно другого списку та навпаки без повторень. Роздрукувати підсумковий
# об'єкт на екран в прямій послідовності, зворотній, а також виконати сортування за зростанням та спаданням.

rng_1 = int(input("How many numbers do you want to put inside of the FIRST list? "))
lst_1, lst_2 = [], []

for i in range(rng_1):
    lst_1.append(int(input(f"Write your number No.{i + 1}: ")))

rng_2 = int(input("How many numbers do you want to put inside of the SECOND list? "))

for j in range(rng_2):
    lst_2.append(int(input(f"Write your number No.{j + 1}: ")))

st_1, st_2 = set(lst_1), set(lst_2)

st_1_in_2 = st_1.difference(st_2)
st_2_in_1 = st_2.difference(st_1)

rcvd_lst = list(st_1_in_2.union(st_2_in_1))
rvrsd_lst = rcvd_lst.copy()
rvrsd_lst.reverse()
print(f"There are the following lists, combined from the both lists, given above:\n\tThe list of unique values: "
      f"{rcvd_lst},\n\tThe list of reversed unique values: {rvrsd_lst},\n\tThe list of unique values in ascending "
      f"order: {sorted(rcvd_lst)},\n\tThe list of unique values in descending order: {sorted(rcvd_lst, reverse=True)}.")
