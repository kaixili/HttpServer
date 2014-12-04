import ssl, socket, time
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(certfile='server.pem')
                        
bindsocket = socket.socket()
bindsocket.bind(('127.0.0.1', 443))
bindsocket.listen(5)

newsocket, fromaddr = bindsocket.accept()
connstream = context.wrap_socket(newsocket, server_side=True)

try:
    data = connstream.recv(1024)
    print(data)
    buf = 'Hi NN%f\n\n\n\n'%time.time()
    buf = buf.encode()
    connstream.send(buf)
finally:
    connstream.shutdown(socket.SHUT_RDWR)
    connstream.close()
    bindsocket.close()