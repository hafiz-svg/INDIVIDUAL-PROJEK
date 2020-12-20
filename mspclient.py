import socket
#take server name and port name
host = "192.168.56.105"
port = 18
#create socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Waiting for connection....")
#connect to server and port number
try:
	client.connect((host, port))
except socket.error as e:
	print(str(e))
#receive message
Response = client.recv(1024)
print(Response)
#input message to send
Input = input("Enter message to the server :")
#send the message to server
client.send(Input.encode("utf-8"))
print("Client has been disconnect")
client.close()
