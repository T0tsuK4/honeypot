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
    # Implemente sua lógica de análise de tráfego aqui
    # Por exemplo, você pode verificar padrões específicos, extrair informações relevantes, etc.
    # Você pode usar bibliotecas como Scapy para análise mais avançada de pacotes de rede.
    pass

def honeypot(port):
    # Crie um socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Defina a opção de reutilização do endereço para permitir a rápida reinicialização
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Associe o socket ao endereço localhost e à porta especificada
    server_socket.bind(('localhost', port))
    
    # Aguarde por conexões
    server_socket.listen(5)
    
    print(f"Aguardando conexões na porta {port}...")
    
    while True:
        # Aceite a conexão de um cliente
        client_socket, client_address = server_socket.accept()
        
        # Inicie uma thread para lidar com o cliente
        client_thread = threading.Thread(target=acao_cliente, args=(client_socket, client_address))
        client_thread.start()

# Execute o honeypot na porta 8080
honeypot(8080)
