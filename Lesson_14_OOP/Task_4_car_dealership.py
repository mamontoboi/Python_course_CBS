# Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів,
# доступних для продажу, і функцію продажу заданого автомобіля.

class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand.lower()
        self.model = model.lower()
        self.year = str(year).lower()
        self.price = str(price).lower()
        Dealership.total += 1
        Dealership.list_of_cars.append(f"{self.brand} {self.model}")

    def sell_car(self):
        try:
            Dealership.list_of_cars.remove(self)
            Dealership.total -= 1
            print(f"{self} was sold. The list was updated.")
            Dealership.print_stock()
        except ValueError:
            print("Not in stock")


class Dealership:
    list_of_cars = []
    total = 0

    @staticmethod
    def print_stock():
        print(f"Total number of cars in the dealership is {Dealership.total}.\nThose are the cars available: \n"
              f"{Dealership.list_of_cars} \n")


jaguar = Car('jaguar', 'i-pace', 2019, 83000)
kia = Car('kia', 'stringer', 2021, 45000)
jaguar_e = Car('jaguar', 'e-type', 1961, 215000)

action = input("Do you want to add new car? yes/no \n").lower()
if action == 'yes':
    new_car = Car(input("Write the brand of the car: "), input("Write the model of the car: "),
                  input("Write the year of manufacturing: "), input("Write the estimated price: "))

Dealership.print_stock()

Car.sell_car('kia stringer')

Car.sell_car(input("Write the brand and model of the car you want to sell: ").lower())
