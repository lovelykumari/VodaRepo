#Include Package
import socket

#2. Prepare Socket
s=socket.socket()
print("Socket Created")

#3.Bind to Server Machine
remoteDetail=("",1234)
s.bind(remoteDetail)
print("Socket Binded on Port 1234")

#4. Listing Mode
s.listen(5)
print("Socket Server Listing")

while True:
    c,addr=s.accept()
    print("Got Connect From ",addr)

    clientGreetMsg="Thanks for Joining..."

    c.send(clientGreetMsg.encode())
    
    c.close()
    print("Client Connect Closed")