# Створіть прототип програми «Бібліотека», в якій є можливість перегляду та внесення змін до структури:
# прізвище:
# посада: ...
# досвід роботи: …
# портфоліо: …
# коефіцієнт ефективності: …
# стек технологій: …
# зарплата: …
# Передбачте можливість виведення на екран сортування за прізвищем та найефективнішим співробітником.

library = {}

library['Employee_1'] = {
    'name' : 'Corey',
    'surname' : 'Schafer',
    'position' : 'Youtuber',
    'experience' : 10,
    'portfolio' : 'youtube/CoreyMS',
    'productivity' : '95',
    'technology' : 'Python',
    'salary' : 120000
}
library['Employee_2'] = {
     'name' : 'Chuck',
     'surname' : 'Severance',
     'position' : 'PhD',
     'experience' : 30,
     'portfolio' : 'py4e',
     'productivity' : '90',
     'technology' : 'Python',
     'salary' : 150000
}
count = 2

choice_1 = input("Do you want do ADD new employee to the library or to MODIFY the existing ones? "
                 "Press Enter to SKIP\n").upper()
while choice_1 == 'ADD' or choice_1 == 'MODIFY':
    if choice_1 == 'ADD':
        count += 1
        library[f'Employee_{count}'] = {}
        Employee = {}
        print("Please state the following data or put N/A:")
        name = input("What is the employee's name? ").title()
        surname = input("What is the employee's surname? ").title()
        position = input("What is the employee's position? ")
        experience = input("How many years of experience has the employee? ")
        portfolio = input("What is the employee's portfolio? ")
        productivity = input("What is the employee's productivity? ")
        technology = input("What is the technology the employee is expirienced in? ")
        salary = input("What is the employee's salary? ")
        Employee.update({'name': name, 'surname' : surname,
                         'position' : position, 'experience' : experience,
                         'portfolio' : portfolio, 'productivity' : productivity,
                         'technology' : technology, 'salary' : salary})
        library[f'Employee_{count}'] = Employee
        for key, value in library.items():
            print(key, value)
        choice_2 = input("Do you want to ADD more? \n").title()
        if choice_2 == 'ADD':
            continue
        else:
            break
    elif choice_1 == 'MODIFY':
        print("Check the current list of employees and write the ID of employee whose data you'd like to modify.")
        for key, value in library.items():
            print(key, value)
        choice_3 = input("Write his ID here (e.g. Employee_1):\n")
        choice_4 = input("What data you'd like to change? ")
        library[choice_3][choice_4] = input("Write the new data: ")
        choice_5 = input("Do you want to modify something else? Yes/No \n").title()
        if choice_5 == 'Yes':
            continue
        else:
            break

for key, value in library.items():
    print(key, value)

choice_6 = input("Do you want to make some sorting? Yes/No\n").title()
if choice_6 == 'Yes':
    choice_7 = input("From the list below choose the number of parameter you want to sort the DB by: \n\t1 - for 'name' "
                     "\n\t2 - for 'surname' \n\t3 - for 'position' \n\t4 - for 'experience' \n\t5 - for 'productivity'"
                     " \n\t6 - for 'technology' \n\t7 - for 'salary'\n")

    match choice_7:
        case '1':
            sorted_by_name = sorted(library.values(), key=lambda value: value['name'])
            print("This is the list of employees, sorted by their names in alphabetical order:")
            for element in sorted_by_name:
                print(element)
        case '2':
            sorted_by_surname = sorted(library.values(), key=lambda value: value['surname'])
            print("This is the list of employees, sorted by their surnames in alphabetical order:")
            for element in sorted_by_surname:
                print(element)
        case '3':
            sorted_by_position = sorted(library.values(), key=lambda value: value['position'])
            print("This is the list of employees, sorted by positions in alphabetical order:")
            for element in sorted_by_position:
                print(element)
        case '4':
            sorted_by_experience = sorted(library.values(), key=lambda value: value['experience'], reverse=True)
            print("This is the list of employees, sorted by years of experience in descending order:")
            for element in sorted_by_experience:
                print(element)
        case '5':
            sorted_by_productivity = sorted(library.values(), key=lambda value: value['productivity'], reverse=True)
            print("This is the list of employees, sorted by productivity in descending order:")
            for element in sorted_by_productivity:
                print(element)
        case '6':
            sorted_by_technology = sorted(library.values(), key=lambda value: value['technology'])
            print("This is the list of employees, sorted by technology, that they are using:")
            for element in sorted_by_technology:
                print(element)
        case '7':
            sorted_by_salary = sorted(library.values(), key=lambda value: value['salary'], reverse=True)
            print("This is the list of employees, sorted by salary in descending order:")
            for element in sorted_by_salary:
                print(element)
        case _:
            print("Wrong entry.")
    print()
    print("We are happy to announce that you have reached the end of the programme! Congrats!")
else:
    print("We are happy to announce that you have reached the end of the programme! Congrats!")