import subprocess
import time
import socket

# Criar banners e arquivos de log
with open("20.txt", "w") as file:
    file.write("ProFTPD 1.3.4a Server (Debian)")

open("20.log", "w")

with open("21.txt", "w") as file:
    file.write("ProFTPD 1.3.4a Server (Debian)")

open("21.log", "w")

open("22.log", "w")

with open("22.txt", "w") as file:
    file.write("OpenSSH 3.9p1 (protocol 1.99)")

open("53.log", "w")

with open("53.txt", "w") as file:
    file.write("ISC BIND 9.8.2rc1")

print("Opening ports")
time.sleep(5)
subprocess.call("clear", shell=True)

print("Ports open!")
print("")
subprocess.call("netstat -nlpt", shell=True)

while True:
    # Porta 20
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 20))
    s.listen(1)
    conn, addr = s.accept()
    with open("20.log", "a") as log_file:
        log_file.write(str(addr) + " - " + str(time.time()) + "\n")
    conn.sendall(open("20.txt", "rb").read())
    conn.close()

    # Porta 21
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 21))
    s.listen(1)
    conn, addr = s.accept()
    with open("21.log", "a") as log_file:
        log_file.write(str(addr) + " - " + str(time.time()) + "\n")
    conn.sendall(open("21.txt", "rb").read())
    conn.close()

    # Porta 22
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 22))
    s.listen(1)
    conn, addr = s.accept()
    with open("22.log", "a") as log_file:
        log_file.write(str(addr) + " - " + str(time.time()) + "\n")
    conn.sendall(open("22.txt", "rb").read())
    conn.close()

    # Porta 53
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 53))
    s.listen(1)
    conn, addr = s.accept()
    with open("53.log", "a") as log_file:
        log_file.write(str(addr) + " - " + str(time.time()) + "\n")
    conn.sendall(open("53.txt", "rb").read())
    conn.close()
