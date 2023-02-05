from socket import *
from threading import *
import sys
import argparse


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

#print('The server is ready to receive')
while True:
	(connectionSocket, addr) = serverSocket.accept() 
	tempPass = args.passcode
	connectionSocket.send(tempPass.encode())
	
	message = connectionSocket.recv(1024).decode()
	print(message + ' has joined the chatroom.')
	connectionSocket.close()
	#messages = connectionSocket.recv(1024).decode()
	#if(messages == ":Exit"):
		#connectionSocket.close()
		#print(message + " left the chatroom")
	#else:
		#print(message + ": " + messages)
	


if __name__ == "__main__":
	pass