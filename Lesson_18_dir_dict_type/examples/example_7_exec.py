# exec(object, globals=None, locals=None)
# Параметри:
# object - рядок коду, або об'єкт коду,
# globals - словник глобального простору, щодо якого слід виконати код,
# locals - об'єкт-відображення (наприклад dict), локальне місце, у якому слід виконати код.
# Функція exec() підтримує динамічне виконання Python і приймає великі блоки коду, на відміну від eval(). Переданий
# функції код повинен бути рядком, або об'єктом коду, наприклад згенерований функцією compile(). Якщо це рядок, то
# рядок аналізується як набір операторів Python, який потім виконується (якщо не виникає синтаксична помилка). Якщо це
# об'єкт коду, він просто виконується. У всіх випадках очікується, що код, що виконується, буде дійсним, як введення
# файлу.
#
# У всіх випадках, якщо глобальні та місцеві організації опущені, код виконується в поточній області видимості. Якщо
# вказуються глобальні змінні, це має бути словник (а не підклас словника), який використовуватиметься як для
# глобальних, так і для локальних змінних. Якщо передаються локальні змінні, місцеві організації можуть бути будь-яким
# відображаючим об'єктом.
#
# Увага:
#
# Пам'ятайте, що інструкції return та yield не можуть бути використані поза визначенням функцій, навіть у контексті
# коду, переданого exec().
# Пам'ятайте, що на рівні модуля globals і locals - той самий словник. Якщо функція отримає різні об'єкти в Globals і
# Locals, код буде виконаний, якби він був розташований в оголошенні класу.
# Якщо словник globals не містить значення для ключа __builtins__, передається вбудований builtins простір. Таким
# чином, ви можете контролювати, які вбудовані функції доступні для виконуваного коду, вставляючи власний __builtins__
# словник у глобальні змінні перед його передачею exec().
#
# Вбудовані функції globals() і locals() повертають поточний глобальний та локальний словник, відповідно, які можуть
# бути корисні для передачі як globals і locals аргументів функції exec().
# Не слід намагатись модифікувати словник locals(). Якщо потрібний вплив коду exec() на локальну область, явно
# передавайте словник locals.
x = 'name = "Ivan"\nprint(name)'
# John
exec(x)
y = 'print("15 - 5 =", (25 - 10))'
# 15 - 5 = 15
exec(y)
program = 'for x in range(9):\n\tres = x * x\n\tprint(res)'
exec(program)
