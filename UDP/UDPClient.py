#UDPClient.py

from socket import socket, SOCK_DGRAM, AF_INET

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input lowercase sentence: ')
clientSocket.settimeout(1)


#send data
clientSocket.sendto(message, (serverName, serverPort))

try:
    #receive response
    modifiedMessage, addr = clientSocket.recvfrom(2048)
    print (modifiedMessage, addr)
except:
    print ("REQUEST TIMED OUT")
    #Allow the client to give up if no response has been reveived within 1 second.
    inputTimeOut = raw_input("Do you want to continue, or exit. Type any value to exit\n")        
    #exit
    if inputTimeOut == "[e]":
        clientSocket.close()

clientSocket.close()


