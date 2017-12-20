#----------------------------------------UDP Test Client Code-----------------------------------------------#
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Minchael', b'Tragy', b'Clown']:
    s.sendto(data, ('127.0.0.2', 9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
