#!/usr/bin/python
import socket

f = open("sockData.txt","a")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def getNum(line):
        return int(line.split(": ")[1])

def operacion(a,b,c):
        return (a + b)*c



s.connect(("192.168.55.101",8888))


t = s.recv(1024).decode()
f.write(t)

print(t)

a1=0
a2=0
a3=0

f.close()
x = open("sockData.txt","r")




for line in t.splitlines():
        print(line)
        if "First" in line:
                a1 = getNum(line)
                print("a1: "+str(a1))
        elif "Second" in line:
               a2 = getNum(line)
        elif "Third" in line:
                a3 = getNum(line)

s.send(str(operacion(a1,a2,a3)).encode())

print("enviado: "+ str(operacion(a1,a2,a3)))
print(s.recv(1024).decode())

#s.send("CRASH!!".encode())
#print(s.recv(1024).decode())
