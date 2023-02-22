import socket
'''There are no handshaking in UDP protocol. No .accept from the server's side, no .connect from the side of client. 
And no .close() at the end. But instead of .send and .recv .sendto and .recvfrom to be used. Also buffer size matters
more while using UDP, as in case the predetermined buffer exceeded the whole data being transferred will be lost'''

HOST = ''  # local IP may be identified here
PORT = 5750

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = (HOST, PORT)

server.bind((HOST, PORT))  # server start listening for messages coming in

while True:
    message, address = server.recvfrom(4096)
    if not message:
        break
    print(f'The following was received from {address}:')
    print(f"The new device, {message.decode('utf-8')}, was detected and installed.")
    server.sendto(f"The new device, {message.decode('utf-8')}, was successfully installed.".encode('utf-8'), address)
