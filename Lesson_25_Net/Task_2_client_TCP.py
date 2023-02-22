import socket

gadgets = ['phone', 'another phone', 'one more phone']

HOST = '127.0.0.1'
PORT = 5750

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

for i in gadgets:
    client.send(i.encode('utf-8'))
    result = client.recv(1024).decode('utf-8')
    print(result)

print("All data was successfully transmitted.")
client.close()

