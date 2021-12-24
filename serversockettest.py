import socket

s = socket.socket()

s.bind(('localhost', 9999))

s.listen(3)

print("Server is listening for incoming connections...")

while True:
    c, address = s.accept()
    name = c.recv(1024).decode()

    print("incoming connection from address ...", address, name)



    c.send(bytes("Hi there!!", 'utf-8'))
    c.close()
