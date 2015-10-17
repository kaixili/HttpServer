import socket, select

response  = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('', 8080))
serversocket.listen(1)
serversocket.setblocking(0)
serversocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) #不要缓存 立即发送

epoll = select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)

try:
    connections = {}; requests = {}; responses = {}
    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            if fileno == serversocket.fileno():
                connection, address = serversocket.accept()
                connection.setblocking(0)
                
                epoll.register(connection.fileno(), select.EPOLLIN)
                connections[connection.fileno()] = connection
                
                requests[connection.fileno()] = b''
                responses[connection.fileno()] = response
                
            elif event & select.EPOLLIN:
                requests[fileno] += connections[fileno].recv(1024)
                if b'\n\n' in requests[fileno] or b'\n\r\n' in requests[fileno]:
                    epoll.modify(fileno, select.EPOLLOUT)
                    connections[fileno].setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)
                    print('FROM{1} \n{0}'.format(requests[fileno].decode(), address))

            elif event & select.EPOLLOUT:
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
                    connections[fileno].setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 0)
                    epoll.modify(fileno, 0)
                    connections[fileno].shutdown(socket.SHUT_RDWR)
                    
            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
   epoll.unregister(serversocket.fileno())
   epoll.close()
   serversocket.close()