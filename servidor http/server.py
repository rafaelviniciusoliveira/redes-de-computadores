
import socket

HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.bind((HOST, PORT))# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.listen(1)# "escuta" pedidos na porta do socket do servidor

print ('Serving HTTP on port %s ...' % PORT)# imprime que o servidor esta pronto para receber conexoes

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)
    aux = request.decode('utf-8')

    # imprime na tela o que o cliente enviou ao servidor
    print (request.decode('utf-8'))
   
    vetor0 = aux.split(" ")[0]
    vetor1 = aux.split(" ")[1]
 
    if vetor0 == 'GET':
        if vetor1 != '/index.html' and vetor1 != '/':
            arquivo=open('notfound.html') # abre o arquivo de texto
            html_response = arquivo.read()
            http_response = "HTTP/1.1 404 Not Found\r\n\r\n" + html_response
            client_connection.send(http_response.encode('utf-8'))
        else:
            if vetor1 == '/index.html':
                arquivo = open('index.html') # abre o arquivo de texto
                html_response = arquivo.read()
                http_response = "HTTP/1.1 200 OK\r\n\r\n" + html_response
                client_connection.send(http_response.encode('utf-8'))
     
    if vetor0 == 'GET' and vetor1 == '/':
        arquivo= open('index.html') # abre o arquivo de texto
        html_response = arquivo.read()
        http_response = "HTTP/1.1 200 OK\r\n\r\n" + html_response  
        client_connection.send(http_response.encode('utf-8'))

    if vetor0 == 'HEAD' or vetor0 == 'POST' or vetor0 == 'PUT' or vetor0 == 'DELETE' or vetor0 == 'TRACE' or vetor0 == 'CONNECT' or vetor0 == 'OPTIONS':
        arquivo= open('badrequest.html') # abre o arquivo de texto
        html_response = arquivo.read()
        http_response = "HTTP/1.1 400 Bad Request\r\n\r\n" + html_response
        client_connection.send(http_response.encode('utf-8'))
    
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()