from socket import *
from threading import *
import sys
import argparse

#Command​: python3 client.py -join -host <hostname> -port <port> -username <username> -passcode <passcode>
#Output​ (on Server): <username> joined the chatroom


#TODO: Implement a client that connects to your server to chat with other clients here

# Takes in IP address, listening port, username, password(same password max 5 letters)
#If correct password, client prints "Connected to <hostname> on port <port>"; Otherwise, "Incorrect passcode"
#When new client joins chatroom, all other clients should receove message indicating username of new user
# Use sys.stdout.flush() after print statemtents

#Output​ (on new Client): Connected to <hostname> on port <port>

parser = argparse.ArgumentParser()
parser.add_argument('-join', action='store_true')
parser.add_argument('-host')
parser.add_argument('-port', type=int)
parser.add_argument('-username')
parser.add_argument('-passcode')
args = parser.parse_args()

serverName = args.host
serverPort = args.port
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

#Receive the password from the server
def sendMessage():
	message = input()
	while True:
		clientSocket.send(message.encode())
		message = input()
		if (message == ":Exit"):
			clientSocket.send(message.encode())
			break
	clientSocket.close()
	return

def recvMessage(userName):
	while True:
		message = clientSocket.recv(1024).decode()
		sys.stdout.flush()
		if message.split(':')[0] == userName:
			pass
		elif message == userName + ' left the chatroom':
			return
		elif message == userName + ' joined the chatroom':
			pass
		else:
			print(message)
			sys.stdout.flush()
	return



tempPass = clientSocket.recv(1024).decode()
if (args.passcode == tempPass): #Validate the password
	userName = args.username
	#portNumber = clientSocket.recv(1024)
	clientSocket.send(userName.encode())

	portNumber = clientSocket.recv(1024)
	print('Connected to ' + args.host + ' on port ' + str(args.port)) #If validated, say connected to which host and port
	sys.stdout.flush()

	send = Thread(target=sendMessage)
	send.start()

	recv = Thread(target = recvMessage, args = (userName,))
	recv.start()
else :
	print("Incorrect passcode")
	sys.stdout.flush()
	clientSocket.close()
	


sys.stdout.flush()


if __name__ == "__main__":
	pass
