import socket
import os
from _thread import *

#host name and port number
host = '192.168.56.104'
port = 18

#create socket 
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ThreadCount = 0
#bind socket with server and port number
try:
	server.bind(('', port))
except socket.error as e:
	print(str(e))
print("Waiting for connection")
#allow maximun 5 connection
server.listen(5)

def threaded_client(c):
	print("CONNECTION FROM: ", str(addr))
	#send mesage to client with encoding into string
	c.send(str.encode("Connected to server.."))
	#receive message string form at 2048 bytes
	data = c.recv(2048)
	#check data
	if not data:
           print("No message received")
	else:
           msg = data.decode()
           print ("Client message:", msg)
	print ("CLient at" ,addr, "disconnected..")
	c.close()
while True:
	#wait client accept
    c, addr = server.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    start_new_thread(threaded_client, (c, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
server.close()
