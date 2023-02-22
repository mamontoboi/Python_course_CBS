# Створіть сокет, який приймає повідомлення з двома числами, що розділені комою.
# Сервер має конвертувати рядкове повідомлення у два числа й обчислювати його суму.
# Після успішного обчислення повертати відповідь клієнту.

import socket

HOST = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(5)
    conn, address = server.accept()
    print("Communication established")
    numbs = conn.recv(1024).decode('utf-8')
    x, y = numbs.split(', ')
    try:
        total = int(x) + int(y)
    except ValueError:
        print("Wrong data!")
        exit(1)
    else:
        conn.send(str(total).encode('utf-8'))
    finally:
        print("Communication completed")
