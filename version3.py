import optparse
import os
import socket
import time
from threading import Thread
from io import StringIO

from data2 import content_type, responses_stat #2个字典数据

host, port = '', 10000

location = '/home/lkx810/b'


def server(client, address):
    def send_bytes(responses, data):   #文件发送
        client.send(bytes('HTTP/1.1 {0} {1}\r\n'.format(responses, responses_stat[responses][0]), 'UTF-8'))
        client.send(bytes("Content-Type: {0}\r\n\r\n".format(content_type[target[-3:]]), 'UTF-8'))
        client.send(bytes(data, 'UTF-8'))
    
    data = client.recv(1024)
    print('{0} From {1}'.format(data.decode('utf-8'), address)) 
    if not data:
        data_request_method = data.decode('utf-8').split()[0]
        if data_request_method == 'POST':
            print('\t POST_DATA:' + data.decode('utf-8').split()[-1])
        data_request_address = data.decode('utf-8').split()[1]
    
        if data_request_address[-1] == '/':
            data_request_address += 'index.html' 
        elif data_request_address[0] != '/':
            send_bytes(411, '')
            pass
    
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
    



def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #IPv4(AF_INET，IP version 4)和TCP协议(SOCK_STREAM)
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #非阻塞模式
    s.bind((host,port))
    s.listen(1024)
    print("HTTP server at:{0}:{1}".format(host, port))
    while True:
        client, address = s.accept()
        thread = Thread(target = server, args = [client, address])
        thread.setDaemon(True)
        thread.start()
    
if __name__ == '__main__':
    main()
    