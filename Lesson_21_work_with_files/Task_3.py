# Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON.

import pickle

data_dict = {'bla': 2000, 'blabla': 4000, 'blablabla': 6000}

pickle_out = open("data.json", "wb")
pickle.dump(data_dict, pickle_out)
pickle_out.close()

with open("data.json", 'rb') as pickle_in:
    new_dict = pickle.load(pickle_in)
    print(new_dict)
