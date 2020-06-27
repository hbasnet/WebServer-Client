
# Import socket module
import socket
import sys
import datetime
# Import thread module
import threading

# Create a TCP server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  

# Assign a port number
serverPort = sys.argv[1]

# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))

# Listen to at most 5 connection at a time
serverSocket.listen(5)

# Server should be up and running and listening to the incoming connections
def multi_thread(connectionSocket):
    try:

        # Extract the path of the requested object from the message


        message = connectionSocket.recv(1024).decode('utf-8')

        f = open(message,'rb')

        # Store the entire contenet of the requested file in a temporary buffer

        outputdata = f.read()


        # Send the HTTP response header line to the connection socket


        # Send the content of the requested file to the connection socket


    # Close the socket in case of some issues 
    connectionSocket.close()


while True:
    '''This part is for multi threading'''
    print 'Ready to serve'
    '''Start the new thread'''







