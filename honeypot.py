import socket
import threading
import datetime

def acao_cliente(client_socket, client_address):

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Conexão recebida de {client_address[0]}:{client_address[1]} em {current_time}")
    
    with open("honeypot_log.txt", "a") as log_file:
        log_file.write(f"Conexão recebida de {client_address[0]}:{client_address[1]} em {current_time}\n")
    
    response = "Bem-vindo ao honeypot!\n"
    client_socket.send(response.encode())
    
    while True:
        data = client_socket.recv(1024)
        
        if not data:
            break
        
        with open("honeypot_log.txt", "a") as log_file:
            log_file.write(f"Dados recebidos de {client_address[0]}:{client_address[1]} em {current_time}:\n")
            log_file.write(data.decode())
            log_file.write("\n")
        
        analise_trafego(data)
        
        response = "Obrigado por sua solicitação.\n"
        client_socket.send(response.encode())
    
    client_socket.close()

def analise_trafego(data):
    
    pass

def honeypot(port):
    #Socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(('localhost', port))
   
    server_socket.listen(5)
    
    print(f"Aguardando conexões na porta {port}...")
    
    while True:
        
        client_socket, client_address = server_socket.accept()
        
        client_thread = threading.Thread(target=acao_cliente, args=(client_socket, client_address))
        client_thread.start()

honeypot(8080)
