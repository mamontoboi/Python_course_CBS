# Створіть програму спортивного комплексу, у якій передбачене меню: 1 - перелік видів спорту, 2 - команда тренерів,
# 3 - розклад тренувань, 4 - вартість тренування. Дані зберігати у словниках. Також передбачити пошук по прізвищу
# тренера, яке вводиться з клавіатури у відповідному пункті меню. Якщо ключ не буде знайдений,
# творити відповідний клас-Exception, який буде викликатися в обробнику виключень.

fighting_styles = ['Boxing', 'Muay-Thai', 'Karate', 'Taekwondo']


class NotFound(Exception):
    def __str__(self):
        return "The mentioned trainer is not in the list of available trainers"


sportcomplex = {
    'Trainers': {
        'Jax': fighting_styles[0],
        'Jacqui Briggs': fighting_styles[1],
        'Johnny Cage': fighting_styles[2],
        'Sonya Blade': fighting_styles[3]
    },
    'Schedule': {
        fighting_styles[0]: '10:00',
        fighting_styles[1]: '11:30',
        fighting_styles[2]: '13:00',
        fighting_styles[3]: '15:30'
    },
    'Price': {
        fighting_styles[0]: 100,
        fighting_styles[1]: 150,
        fighting_styles[2]: 130,
        fighting_styles[3]: 140
    }
}
def interact():
    while True:
        action = input(
"""                                                  
Choose what you'd like to know:                               
\t1. List of martial arts available for training             
\t2. Trainers and martial arts they are teaching             
\t3. Schedule of Classes                                     
\t4. Price per Training Session                              
\t5. Exit the menu                                           
""")

        match action:
            case '1':
                print("This is the list of all available martial classes: ", *fighting_styles)
                interact()
            case '2':
                print("This is the list of our trainers: \n")
                for i in sportcomplex['Trainers'].keys():
                    print(i)
                print()
                req_trainer = input('What trainer do you what to know about? \n ').capitalize()
                try:
                    print(f"\tThis is the class where {req_trainer} is teaching: {sportcomplex['Trainers'][req_trainer]}")
                except KeyError:
                    raise NotFound
            case '3':
                print("This is the list of available classes: \n")
                for key, value in sportcomplex['Schedule'].items():
                    print(f'\t{key} at {value}')
                print()
            case '4':
                print("The prices for the classes are as follows: \n")
                for key, value in sportcomplex['Price'].items():
                    print(f'\t{key} costs {value} per training session')
                print()
            case '5':
                break
            case _:
                interact()
    print("Thank you for choosing our Fight Club!")


if __name__ == '__main__':
    interact()
