import socket

# host = socket.gethostbyname(socket.gethostname())  # to determine a dynamic IP (will adjust himself on each machine)
HOST = ''  # to listen on all possible channels of data. Can be local on server. Must be global on client.
PORT = 5750

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(9)  # 9 -- length of queue. Puts on hold 9 more requests, while it's busy. Rejects the further calls.

communication_socket, address = server.accept()  # establishment of handshaking. .connect from the side of client
print(f"Communication socket with {address} established")

while True:
    message = communication_socket.recv(1024).decode('utf-8')
    if not message:
        break
    print(f'New device, {message}, is detected.')
    communication_socket.send(f"The new device - {message} - was successfully installed.".encode('utf-8'))

print('Connection completed')
communication_socket.close()  # connection must be closed after completion of operation. Context managers can be used.


