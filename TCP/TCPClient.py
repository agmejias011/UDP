#source: https://pymotw.com
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 12001)
print >>sys.stderr, 'connecting to %s port %s' % server_address
print("Type ""CTRL+C"" to finish")

#connecting to server
sock.connect(server_address)

#getting the username of the user
username = raw_input("Username: ");

while True:
    try:
        # Send data
        message = raw_input("{}: ".format(username))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
    
        #checking if any message was sent
        while amount_received < amount_expected:
            data = sock.recv(2048)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data
    except KeyboardInterrupt:
        print ("Interrupted by CTRL+C")        

sock.close()
