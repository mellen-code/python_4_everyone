import socket

# create socket communication line for this program
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# create connection to server via port 80
mysock.connect(('data.pr4e.org', 80))

# store get request in variable, encode in bytes
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

# send get request through connection
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()