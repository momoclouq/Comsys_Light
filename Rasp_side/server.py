import socket

HOST = '10.247.211.134'
PORT = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error:
    print('bind failed')

s.listen(1)
print("Socket wait message")
(conn, addr) = s.accept()
print("connected")

while True:
    data = conn.recv(1024).decode()
    #print ("I sent a message back in response to: " + data)

    if data == "hello":
        reply = "hi, back"
    elif data == "this is important":
        reply = "important indeed"
    elif data == "quit":
        conn.send(("end").encode())
        break
    else:
        reply = "unknown command"

    conn.send(reply.encode())
conn.close()