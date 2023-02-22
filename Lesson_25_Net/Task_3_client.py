import socket

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

data = (input("Please write first number: ") + ', ' + input("Please write second number: "))
client.send(data.encode('utf-8'))
message = client.recv(1024).decode('utf-8')
print(f'The sum of {data [0]} and {data[-1]} is {message}.')
