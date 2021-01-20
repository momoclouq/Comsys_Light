import socket

HOST = '10.247.211.134' #ip or hostname of your server
PORT = 12345 #any open port (above 1000), must math with server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    command = raw_input('Enter command:')
    s.send(command.encode())
    reply = s.recv(1024).decode()
    if reply == "terminate":
        break;
    print reply