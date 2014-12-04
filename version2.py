import socket
from socketserver import ThreadingMixIn


content_type={
    ".js" : "application/x-javascript",
    "jpg" : "image/jpg",
    "gif" : "image/gif",
    "css" : "text/css",
    "tml" : "text/html"
}




host = ''
port = 80
backlog = 255
size_max = 1024

location = '/home/lkx810/b'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建socket对象，并说明使用的是IPv4(AF_INET，IP version 4)和TCP协议(SOCK_STREAM)。
s.bind((host,port))
s.listen(backlog)

while 1:
    try:
        client, address = s.accept() #监听端口
    except KeyboardInterrupt:
        s.close()

    data = client.recv(size_max)
    print('{0} From {1}'.format(data, address))
    
    if not data:
        continue
    data_request_address = str(data).split(' ')[1]
    if data_request_address == '/':
        data_request_address = '/index.html'
        
    target = location
    for i in data_request_address.split('/')[1:]:
            target = target + '/' + i
    print('target---->{0}'.format(target))
    if data:
        try:
            try:
                with open(target) as data_send:
                    client.send(bytes('HTTP/1.0 200 OK\r\n', 'UTF-8'))
                    client.send(bytes('HTTP/1.0 200 OK\r\n', 'UTF-8'))
                    client.send(bytes("Content-Type: {0}\r\n\r\n".format(content_type[target[-3:]]), 'UTF-8'))
                    client.send(bytes(data_send.read(), 'UTF-8'))
            except UnicodeDecodeError:
                #with open(target, 'rb') as data_send:
                 #   client.send(bytes('HTTP/1.0 200 OK\r\n', 'UTF-8'))
                  #  client.send(bytes("Content-Type:{0}\r\n\r\n".format(content_type[target[-3:]]), 'UTF-8') + data_send.read())
               
                data_send = b'''HTTP/1.x 200 OK
Content_Type:image/gif/

'''
                f = open(target, 'rb').read()
                data_send = data_send + f
                client.sendall(data_send)
                
        except FileNotFoundError:
            page404 = location + '/404.html'
            with open(page404) as data_send:
                client.send(bytes('HTTP/1.0 404 Not Found\r\n', 'UTF-8'))
                client.send(bytes("Content-Type: text/html\r\n\r\n", 'UTF-8'))
                client.send(bytes(data_send.read(), 'UTF-8'))
    
    client.close()
    print()