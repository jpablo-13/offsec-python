#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.50.101","9999"))

#we use a 1024 bytes buffer to receive data
#server sends data in binary, we have to decode it, using decode()
s.recv(1024).decode()

#we send a number to be squared (the service running on 192.168.50.101:9999 does this)
s.send("5".encode())

#we receive and print the response
print(s.recv(1024).decode())
s.close()



