#UDPServer.py

#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.
from socket import socket, SOCK_DGRAM, AF_INET
import time, random


#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

while True:
    print ("Waiting for connections")
    # Receive the client packet along with the address it is coming from
    start = time.time()
    message, address = serverSocket.recvfrom(2048)
    # Capitalize the message from the client
    print (message, address)
    message = message.upper()
    end = time.time()

    #Include information about how long each response took. This will be the RTT.
    RTT = end - start
    randomDrops = random.randint(1, 6)

    #Configure the server so that it randomly drops packets when randomDrops equals 1 or 6
    if randomDrops != 1 and randomDrops != 6:
        serverSocket.sendto((message + " , RTT = {}".format(RTT)), address)
    
serverSocket.close()
