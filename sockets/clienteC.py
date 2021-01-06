from socket import * 
serverName = 'localhost'
serverPort = 61000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = input('Digite o seu comando: ')
clientSocket.send(sentence.encode('Utf-8'))
comando = clientSocket.recv(1024) 
clientSocket.close()