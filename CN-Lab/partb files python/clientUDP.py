from socket import *

# Server details
serverName = "127.0.0.1"
serverPort = 12000

# Create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Input file name
sentence = input("Enter file name: ")

# Send the file name to the server
clientSocket.sendto(sentence.encode(), (serverName, serverPort))

# Receive file contents from the server
filecontents, serverAddress = clientSocket.recvfrom(2048)
print('From Server:', filecontents.decode())

# Close the socket
clientSocket.close()
