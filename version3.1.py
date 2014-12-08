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
        self.socket = sock
        self.done = False

    
    def read_recv(self):
        data = self.socket.recv(1024)
        self.done = True
        print('{0} From {1}'.format(data, self.addr))
        
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
        print('here1')
        self.back = True
    
    def return_file(self):
        try:
            try:
                with open(self.target) as self.data_send:
                    self.self.data_send = self.data_send.read()
                    send_bytes(200, self.data_send)
            except UnicodeDecodeError:
                self.data_send = '''HTTP/1.1 200 OK
Content_Type:{0}

'''.format(content_type[target[-3:]])
                f = open(self.target, 'rb').read()
                self.data_send = bytes(self.data_send, 'utf-8') + f
                self.socket.sendall(self.data_send)
        except FileNotFoundError:
            target = location + '/404.html'
            with open(target) as self.data_send:
                self.data_send = self.data_send.read()
                send_bytes(404, self.data_send)

        
    def send_bytes(self):
        self.socket.send(bytes('HTTP/1.1 {0} {1}\r\n'.format(responses, responses_stat[responses][0]), 'UTF-8'))
        self.socket.send(bytes("Content-Type: {0}\r\n\r\n".format(content_type[target[-3:]]), 'UTF-8'))
        self.socket.send(bytes(self.self.data_send, 'UTF-8'))
                

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
            print('here')
            (rs, ws, _) = select.select(rlist, wlist, [])  #what's it? what's happened?
            try:
                for r in rs:
                    if r == sock:
                        (s, addr) = sock.accept()
                        clients[s] = Server(addr, s)
                    elif r in clients:
                        print((rs, ws, _))
                        clients[r].read_recv()
                print((rs, ws, _), '2')
                for w in ws:
                    if w in clients:
                        print('!!!!!!!')
                        clients[w].return_file()
            except Exception:
                raise
            print('here3')
            for s in list(clients.keys())[:]:
                if clients[s].done:
                    del clients[s]
            sock.listen(1)
            print('here4')
    except KeyboardInterrupt:
        print("Got CTRL-C, quitting") 
    finally:
        sock.close()

if __name__ == '__main__':
    main()