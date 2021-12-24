import socket

c = socket.socket()

c.connect(('localhost', 9999))

print ("connected to the server ...")

name = str(input('key in your name :'))

c.send(bytes(name, 'utf-8'))

print(c.recv(1024).decode())
