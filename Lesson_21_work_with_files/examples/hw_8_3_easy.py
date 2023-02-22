# Завдання 3
#
# Створіть список товарів в інтернет-магазині. Серіалізуйте його за допомогою pickle та збережіть у JSON.
import json
import pickle


def main():
    a = """{
        "items":
            [{"name1": "name1",
              "price1": "price1",
              "unit1": "unit1",
              "qty1": "qty1",
              "var1": "('var1', 'var2', 'var3')"},
             {"name2": "name2",
              "price2": "price2",
              "unit2": "unit2",
              "qty2": "qty2",
              "var2": "('var4', 'var5', 'var6')"}]
    }"""
    n = pickle.dumps(a)
    print(n)
    with open('my_data.txt', 'wb') as f:
        pickle.dump(a, f)
    print()

    with open('my_data.txt', 'rb') as fb:
        items = pickle.load(fb)
    print()

    data = json.loads(items)
    print(data)
    with open('my_data.json', 'w') as jb:
        json.dump(data, jb, indent=4)


if __name__ == '__main__':
    main()
