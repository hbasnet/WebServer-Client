
import socket
from time import *
import sys
import time

HOST = sys.argv[1]
PORT = sys.argv[2]
fileName = sys.argv[3]

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print'Client has been established'
server_add = (HOST, int(PORT))

clientSocket.connect(server_add)
# connect the host and port to the socket
##################################################################################
header = {
    "first_header": "GET /%s HTTP/1.1" % (fileName),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-us",
    "Host": HOST,
}
http_header = "\r\n".join("%s:%s" % (
    item, header[item]) for item in header)
print http_header
send_time = time.time()
clientSocket.send("%s\r\n\r\n" % (http_header))
#######################################################################################
data = clientSocket.recv(1024)
recv_time = time.time()
RTT = recv_time - send_time
#print'Data received by the client is', data
print'RTT ', RTT

'''Print other vvalues here '''
''' close socket '''
values = ''
while data:
    values += data
    data = clientSocket.recv(1024)
clientSocket.close()
print " Data received by the client is : ", values
