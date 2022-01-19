#Include Package
import socket

#2. Prepare Socket
s=socket.socket()
print("Socket Created")

#3.Connect to Server
remoteDetail=("127.0.0.1",1234)
s.connect(remoteDetail)
print("Connected to Server")

#Recieve data From the Server
msg=s.recv(1024)
print("SERVER:  ",msg)

s.close()
print("Client Closed")