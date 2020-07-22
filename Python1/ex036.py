import socket
host = socket.gethostname()
ip = socket.gethostbyaddr(host)
print('Endereço de IP: ', ip)
