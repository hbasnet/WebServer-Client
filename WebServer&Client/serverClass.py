import socket
import sys
import datetime
# preparing a socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverPort = int(sys.argv[1])
# now binding socket
serverSocket.bind(('', serverPort))
# listening to the client
serverSocket.listen(5)
while True:
    # Establish a connection
    print 'Ready to serve...'
    # block until there are connections from client
    connectionSocket, address = serverSocket.accept()
    # print f"Connection from {address} is established"
    try:
        msg = connectionSocket.recv(1024)
        print 'messages sent from client: \n', msg
        fname = msg.split()[1]
        f = open(fname[1:])
        # Store the entire contenet of the requested file in a temporary buffer
        outputdata = f.read()
        print "outputdata of the file requested by client: \n ", outputdata
        current = datetime.datetime.now()
        # Send the HTTP response header line to the connection socket
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
         #############################################################################
        # Send the content of the requested file to the connection socket
        i = 0
        while(i < len(outputdata)):
            connectionSocket.send(outputdata[i])
            i += 1
    except socket.error as msg:
        # print "File not found "+str(msg)"
        # sending msg if file is not found
        connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<!doctype html><html><body><h1>404 Not Found<h1></body></html>")
    # Close the socket in case of some issues
    connectionSocket.close()
serverSocket.close()
