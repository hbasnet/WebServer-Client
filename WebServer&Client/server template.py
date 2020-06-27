# Import socket module
import socket
import sys
import datetime
# Import thread module
import threading

# Create a TCP server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assign a port number
serverPort = int(sys.argv[1])

# Bind the socket to server address and server port
serverSocket.bind(('', serverPort))

# Listen to at most 5 connection at a time
serverSocket.listen(5)

# Server should be up and running and listening to the incoming connections


def multi_thread(connectionSocket):
    try:
        # Extract the path of the requested object from the message
        message = connectionSocket.recv(1024)#.decode('utf-8')
        if not message:
            connectionSocket.close()
        print "The message received from client: \n", message
        filename = message.split()[1]
        f = open(filename[1:])
        #f = open(message, 'rb')

        # Store the entire contenet of the requested file in a temporary buffer
        outputdata = f.read()
        print "outputdata:", outputdata

        # Send the HTTP response header line to the connection socket
        current = datetime.datetime.now()
        header = "HTTP/1.1 200 OK"
        #############################################################################
        header_info = {
            "Date": current.strftime("%Y-%m-%d %H:%M"),
            "Content-Length": len(outputdata),
            "Keep-Alive": "timeout=%d,max=%d" % (10, 100),
            "Connection": "Keep-Alive",
            "Content-Type": "text/html"
        }

        following_header = "\r\n".join("%s:%s" % (
            item, header_info[item]) for item in header_info)
        print "following_header:\n", following_header
        connectionSocket.send("%s\r\n%s\r\n\r\n" %
                              (header, following_header))
        #######################################################################
        # Send the content of the requested file to the connection socket
        i = 0
        while(i < len(outputdata)):
            connectionSocket.send(outputdata[i])
            i += 1
    except socket.error as msg:
        #print("File not found "+str(msg))
        # sending msg if file is not found
        connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>")
    # Close the socket in case of some issues
    #connectionSocket.close()


while True:
    '''This part is for multi threading'''
    print 'Ready to serve'
    '''Start the new thread'''
    conn, address = serverSocket.accept()
    print "Connection has been established from " + str(address)
    t = threading.Thread(target=multi_thread(conn))
    t.daemon = True
    t.start()
serverSocket.close()
