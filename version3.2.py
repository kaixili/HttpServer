import socket
import select
import time
from data2 import content_type, responses_stat

location = '/home/lkx810/b'
host = ''
port = 8001

class Server(object):
    def __init__(self, addr, sock):
        self.addr = addr
        self.back = False
        self.target = location +'\404.html'
        self.socket = sock
        self.done = False

    def send_bytes(self, responses, data_send):
        self.socket.send(bytes('HTTP/1.1 {0} {1}\r\n'.format(responses, responses_stat[responses][0]), 'UTF-8'))
        self.socket.send(bytes("Content-Type: {0}\r\n\r\n".format(content_type[self.target[-3:]]), 'UTF-8'))
        self.socket.send(bytes(data_send, 'UTF-8'))
    
    def read_recv(self):
        data = self.socket.recv(1024)
        self.done = True
        print('From {1}\n{0}'.format(data.decode('utf-8'), self.addr))
        
        if not data:
            return
        data_request_file = data.decode('utf-8').strip().split()[1]
        #data_request_method = data.decode('utf-8').split()[0]
        if data_request_file == '/':
            data_request_file += 'index.html'
        #elif data_request_file[0] != '/': 
        #    pass
        
        self.target = location
        for i in data_request_file.split('/')[1:]:
            self.target = self.target + '/' + i
        self.back = True
    
    def return_file(self):
        try:
            try:
                with open(self.target) as self.data_send:
                    self.data_send = self.data_send.read()
                    self.send_bytes(200, self.data_send)
            except UnicodeDecodeError:
                self.data_send = '''HTTP/1.1 200 OK
Content_Type:{0}

'''.format(content_type[self.target[-3:]])
                f = open(self.target, 'rb').read()
                self.data_send = bytes(self.data_send, 'utf-8') + f
                self.socket.sendall(self.data_send)
        except FileNotFoundError:
            self.target = location + '/404.html'
            with open(self.target) as self.data_send:
                self.data_send = self.data_send.read()
                self.send_bytes(404, self.data_send)

                

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #IPv4(AF_INET，IP version 4)和TCP协议(SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #立即复用
    sock.bind((host, port))
    print("HTTP server at:{0}:{1}....waiting....".format('127.0.0.1', port))
    sock.listen(1)  
    
    clients = {}
    try:
        while True:
            rlist = [sock] + list(clients.keys())
            wlist = [s for (s, c) in clients.items() if c.back]
            #(rs, ws, _) = select.select(rlist, wlist, [])  #what's it? what's happened?
            (rs, _, _) = select.select(rlist, [], [])
            try:
                for r in rs:
                    if r == sock:
                        (s, addr) = sock.accept()
                        clients[s] = Server(addr, s)
                    elif r in clients:
                        clients[r].read_recv()
                        clients[r].return_file()
                #for w in ws:
                #    if w in clients:
                #        clients[w].return_file()
            except Exception:
                raise
            for s in list(clients.keys())[:]:
                if clients[s].done:
                    del clients[s]
            sock.listen(1)
    except KeyboardInterrupt:
        print("Got CTRL-C, quitting") 
    finally:
        sock.close()

if __name__ == '__main__':
    main()