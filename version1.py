import socket

host = ''
port = 80
backlog = 5
size = 1024

location = '/home/lkx810/b'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    try:
        client, address = s.accept()
        data = client.recv(size)
        
        print(data, address)
        data_request_address = str(data).split(' ')[1]
        if data_request_address == '/':
            data_request_address = '/index.html'
        
        target = location
        for i in data_request_address.split('/')[1:]:
                target = target + '/' + i
        print(target)
        if data:
            
            try:
                with open(target) as data_send:
                    
                    
                    
                    client.send(bytes('HTTP/1.0 200 OK\r\n', 'UTF-8'))
                    if data_request_address[-3:] =='jpg':
                        client.send(bytes("Content-Type: image/jpeg\r\n\r\n", 'UTF-8'))
                    else:
                        client.send(bytes("Content-Type: text/html\r\n\r\n", 'UTF-8'))
                    client.send(bytes(data_send.read(), 'UTF-8'))
            except NotADirectoryError:
                page404 = location + '/404.html'
                with open(page404) as data_send:
                    client.send(bytes(data_send.read(), 'UTF-8'))
        client.close()
        print('end')
    except KeyboardInterrupt:
        print('end')
        s.close()
1