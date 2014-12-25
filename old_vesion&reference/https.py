import ssl, socket, time
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(certfile='cacert.pem', keyfile='privkey.pem') 
                        
bindsocket = socket.socket()
bindsocket.bind(('127.0.0.1', 443))
bindsocket.listen(1023)

newsocket, address = bindsocket.accept()
connstream = context.wrap_socket(newsocket, server_side=True)

try:
    data = connstream.recv(1024)
    print(data.decode('utf-8') + 'from' + str(address))
    data_send = 'time is %f\n\n\n\n'%time.time()
    
    connstream.send(bytes(data_send,'utf-8'))
finally:
    connstream.shutdown(socket.SHUT_RDWR)
    connstream.close()
    bindsocket.close()