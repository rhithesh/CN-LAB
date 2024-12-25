from socket import *
serverName='127.0.0.1'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input("\n Enter file name :")

clientSocket.send(sentence.encode())
filecontents=clientSocket.recv(1024).decode()
print("\n From Server: \n")
print(filecontents)
clientSocket.close()