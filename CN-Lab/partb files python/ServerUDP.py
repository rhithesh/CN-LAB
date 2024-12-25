from socket import *

# Set up server
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))

print("The server is ready to receive")

# Listen for incoming connections
while True:
    sentence, clientAddress = serverSocket.recvfrom(2048)

    try:
        # Open and read the requested file
        with open(sentence.decode(), "r") as file:
            fileContents = file.read(2048)

        # Send the file contents to the client
        serverSocket.sendto(fileContents.encode(), clientAddress)
        print("Sent back to client:", fileContents)

    except FileNotFoundError:
        errorMessage = "File not found!"
        serverSocket.sendto(errorMessage.encode(), clientAddress)
        print("File not found error sent to client.")
