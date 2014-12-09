import optparse
import os
import socket
import time
import ssl

from threading import Thread
from io import StringIO

from data2 import content_type, responses_stat #2个字典数据

host, port, ssl_port = '', 80, 443
location = os.getcwd() + '/html'

def http_server(client, address, _ssl = 0):
    if _ssl:
        client = _ssl.wrap_socket(client, server_side=True)
    
    def send_bytes(responses, data): 
        client.send(bytes('HTTP/1.1 {0} {1}\r\n'.format(responses, responses_stat[responses][0]), 'UTF-8'))
        client.send(bytes("Content-Type: {0}\r\n\r\n".format(content_type[target[-3:]]), 'UTF-8'))
        client.send(bytes(data, 'UTF-8'))
    
    data = client.recv(1024)
    print('From{1}:\n {0}'.format(data.decode('utf-8'), address), end='')
    
    if data:
        data_request_method = data.decode('utf-8').split()[0]
        if data_request_method == 'POST':
            http_GUI(data.decode('utf-8').split()[-1])
        
        data_get = data.decode('utf-8').split()[1].split('?')
        data_request_address = data_get[0]
        #if len(data_get) != 1:
        #    data_post = '1'
        #    for i in data_get:
        #        try:
        #            data_post += data_get[i]
        #        except:
        #            pass
        #    http_GUI(data_post, address)
                
        
        
        if data_request_address[-1] == '/':
            data_request_address += 'index.html' 
        elif data_request_address[0] != '/':
            send_bytes(411, '<html><head><title>411 - badrequest</title></head><body>411 - badrequest</body></html>')
    
        target = location
        for i in data_request_address.split('/')[1:]:
                target = target + '/' + i
    
        try:
            try:
                with open(target) as data_send:
                    data_send = data_send.read()
                    send_bytes(200, data_send)
                
            except UnicodeDecodeError:
                data_send = '''HTTP/1.1 200 OK
Content_Type:{0}

'''.format(content_type[target[-3:]])  #打不开的文件(图片)二进制 sendall发送
                f = open(target, 'rb').read()
                data_send = bytes(data_send, 'utf-8') + f
                client.sendall(data_send)

        except FileNotFoundError:
            target = location + '/404.html'
            with open(target) as data_send:
                data_send = data_send.read()
                send_bytes(404, data_send)
    
    client.close()
    

def http_GUI(data_post, address):
    print('\n!----RECEIVE SOMETHING FROM{0}:\n          |{1}'.format(address, data_post))
    c = open('post_data', 'w+')
    c.write(data_post)
    c.write('FROM {0}\n'.format(address))
    c.close()



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #IPv4(AF_INET，IP version 4)和TCP协议(SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #非阻塞模式
    s.bind((host,port))
    s.listen(1024)
    print("HTTP server at {0}:{1}".format(host, port))
    
    thread_https = Thread(target = main_https, args = [])
    thread_https.setDaemon(True)
    thread_https.start()
    
    
    while True:
        try:
            client, address = s.accept()
        except KeyboardInterrupt:
            print('GOT CTRL^C, QUITing')
            s.close()
            return -1
        thread = Thread(target = http_server, args = [client, address])
        thread.setDaemon(False)
        thread.start()


def main_https():
    _ssl = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    try:
        _ssl.load_cert_chain(certfile='cacert.pem', keyfile='privkey.pem')
    except:
        print('''ssl error!
            try: openssl req -new -x509 -days 365 -nodes -out cacert.pem -keyout privkey.pem''')
        return -1
    ss = socket.socket()
    ss.bind(('', ssl_port))
    ss.listen(1023)
    print("HTTPS server at {0}:{1}".format(host, ssl_port))
    
    while True:
        try:
            client, address = ss.accept()
        except:
            ss.close()
            return -1
        thread = Thread(target = http_server, args = [client, address, _ssl])
        thread.setDaemon(False)
        thread.start()
        


if __name__ == '__main__':
    if os.path.exists(location + '/index.html'):
        main()
    else:
        print('Please put HTTP files in ../html')
    