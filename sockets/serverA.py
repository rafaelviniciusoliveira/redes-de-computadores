# importacao das bibliotecas
from socket import * # sockets
import time

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    message = message.decode('utf-8')
    if message == 'data': #compara a mensagem recebida com a palavra data.
        modifiedMessage = str(time.ctime()) # Prepara a mensagem com data e hora
        print ('Cliente %s enviou: %s, transformando em: %s' % (clientAddress, message, modifiedMessage))
        serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress) # envia a mensagem modificada para o cliente
# envia a resposta para o cliente
serverSocket.close() # encerra o socket do servidor