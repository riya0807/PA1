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
	
	message = "temp"#socket.recv(1024).decode()
	while message != None:
		message = socket.recv(1024).decode()
		if (message == ":Exit"):
			message = name + " left the chatroom"
			for sock in sockets:
				sock.send(message.encode())
			sockets.remove(socket)
			socket.close()
			message = name + " left the chatroom"
			print(message)
			sys.stdout.flush()
			break
			
		elif (message == ":)"):
			message = name + ": [feeling happy]"
			
		elif (message == ":("):
			message = name + ": [feeling sad]"
		elif (message == ":mytime"):
			currentTime = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
			message = name + ": " + currentTime
		elif (message == ":+1hr"):
			currentTime = datetime.now().strftime("%a %b %d ")
			currentHour = int(datetime.now().strftime("%H"))+1
			currentTime2 = datetime.now().strftime(":%M:%S %Y")
			message = name + ": " + currentTime + str(currentHour) + currentTime2
		else:
			message = name + ': ' + message

		print(message)
		sys.stdout.flush()
		for sock in sockets:
			sock.send(message.encode())

		sys.stdout.flush()
	return

sockets = []
while True:
	(connectionSocket, addr) = serverSocket.accept() 

	tempPass = args.passcode
	connectionSocket.send(tempPass.encode())

	sockets.append(connectionSocket)
	userName = connectionSocket.recv(1024).decode()

	connectionSocket.send(str(args.port).encode())

	message = userName + ' joined the chatroom'
	print(message)
	sys.stdout.flush()
	for sock in sockets:
		sock.send(message.encode())

	
	sys.stdout.flush()
	x = Thread(target = receiveMessages, args=(userName, connectionSocket, ))
	x.start()



if __name__ == "__main__":
	pass
