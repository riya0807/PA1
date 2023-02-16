from socket import *
from threading import *
import sys
import argparse
from datetime import datetime


#TODO: Implement all code for your server here

#Command: ​python3 server.py -start -port <port> -passcode <passcode>
#Output​: Server started on port <port>. Accepting connections

#Takes in listening port and password
# Use sys.stdout.flush() after print statemtents
parser = argparse.ArgumentParser()
parser.add_argument('-start', action='store_true')
parser.add_argument('-port', type=int)
parser.add_argument('-passcode')
args = parser.parse_args()

print('Server started on port ' + str(args.port) + '. Accepting connections')
sys.stdout.flush()

serverPort = args.port
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('',serverPort)) 
serverSocket.listen()

def receiveMessages(name, socket):
	
	clientMessage = socket.recv(1024).decode()
	while clientMessage != None:
		if (clientMessage == ":Exit"):
			socket.close()
			print(name + " left the chatroom")
			sys.stdout.flush()
			return
		elif (clientMessage == ":)"):
			print(name + ": [feeling happy]")
			sys.stdout.flush()
		elif (clientMessage == ":("):
			print(name + ": [feeling sad]")
			sys.stdout.flush()
		elif (clientMessage == ":mytime"):
			currentTime = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
			print(name + ": " + currentTime)
			sys.stdout.flush()
		elif (clientMessage == ":+1hr"):
			currentTime = datetime.now().strftime("%a %b %d ")
			currentHour = int(datetime.now().strftime("%H"))+1
			currentTime2 = datetime.now().strftime(":%M:%S %Y")
			print(name + ": " + currentTime + str(currentHour) + currentTime2)
			sys.stdout.flush()
		else:
			print(name + ': ' + clientMessage)
			sys.stdout.flush()
		clientMessage = socket.recv(1024).decode()
	#sys.stdout.flush()


#print('The server is ready to receive')
while True:
	(connectionSocket, addr) = serverSocket.accept() 
	tempPass = args.passcode
	connectionSocket.send(tempPass.encode())
	
	userName = connectionSocket.recv(1024).decode()
	print(userName + ' joined the chatroom')
	sys.stdout.flush()
	x = Thread(target = receiveMessages, args=(userName, connectionSocket, ))
	x.start()

	connectionSocket.send(str(args.port).encode())

	# clientMessage = connectionSocket.recv(1024).decode()

	# print(clientMessage)
	# sys.stdout.flush()
	
	#connectionSocket.close()
	#messages = connectionSocket.recv(1024).decode()
	#if(messages == ":Exit"):
		#connectionSocket.close()
		#print(message + " left the chatroom")
	#else:
		#print(message + ": " + messages)
	


if __name__ == "__main__":
	pass