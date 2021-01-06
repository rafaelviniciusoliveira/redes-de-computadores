from socket import * 
import os 

serverName = ''
serverPort = 61000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
print("Servidor TCP esperando conexoes na porta %d ..." %(serverPort))

while 1 : 
    connectionSocket, addr = serverSocket.accept()
    comando = connectionSocket.recv(1024)
    comando = comando.decode('Utf-8')

    print("Cliente %s enviou: %s" %(addr,comando))
    os.system(comando)
    connectionSocket.close()
serverSocket.close()