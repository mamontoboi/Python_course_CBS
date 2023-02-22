# Здійснити авторизацію входу користувача в особистий кабінет за такими обліковими даними:
# логін – “Programmer@qew.com”, пароль – “O#wer2Rsdfw!”. Реалізувати обмеження спроб введення пароля.
# # Після 3 неправильних спроб користувач інформується про тимчасове блокування авторизації і запускається
# # процес тимчасового блокування облікового запису.
# Через 5 хвилин блокування знімається, користувач повідомляється про можливість доступу до особистого кабінету.
import time

lgn_act = "Programmer@qew.com"
pwd_act = "O#wer2Rsdfw!"
cnt = 3

while cnt:
    lgn_req = input("Write your login: \n")
    pwd_req = input("Write your password: \n")
    if lgn_req != lgn_act or pwd_req != pwd_act:
        print("Login or password not correct. Try again.")
        cnt -= 1
        if cnt == 0:
            print("Better luck in 5 minutes")
            cnt = 3
            time.sleep(5)
        continue
    else:
        print("You successfully entered useless and meaningless login and password.")
        break












