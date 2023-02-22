import socket

gadgets = ['phone', 'another phone', 'one more phone']

HOST = '127.0.0.1'  # if access to the server is to be made from outside of LAN, global IP to be determined
PORT = 5750
serverAddressPort = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in gadgets:
    client.sendto(i.encode('utf-8'), serverAddressPort)
    print(f'Request to add {i} was sent to the server.')
    message = client.recvfrom(4096)[0].decode('utf-8')
    print(f'The following was received from the server: \n{message}')
