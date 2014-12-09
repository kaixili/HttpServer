import socket
import select

from data2 import content_type, responses_stat

location = '/home/lkx810/b' 
port = 8001
    

class Client(object):
    def __init__(self, addr, sock):
        self.addr = addr
        self._socket = sock
        self._backlog = b''
        self.done = False
 
    def read(self, data):
        """
        This function is meant to be overloaded by classes
        inheriting from Client. It's executed whenever something
        is received from the client.
        """
        ss = data.decode('utf-8', 'replace')
        ss = ss.strip().split()
        print('FROM {1}:\n{0}'.format(ss, self.addr))
        
        request = ss[1]
        if request[-1] == '/':
            request += 'index.html'
        elif request[0] != '/':
            pass
        
        request = location + request
        print(request)
        self.open_file(request)
        
    def open_file(self, target):
        try:
            try:
                with open(target) as data_send:
                    data_send = data_send.read()
                    self.write(data_send, 200, target)
                
            except UnicodeDecodeError:
                f = open(target, 'rb').read()
                
                self.write(data_send, 200, target, 1)
                
        except FileNotFoundError:
            target = location + '/404.html'
            with open(target) as data_send:
                data_send = data_send.read()
                self.write(data_send, 404, target)

        
 
    def write(self, data, responses, target, rb=0):
        self._backlog += bytearray("HTTP/1.1 {0} {1}\r\n".format(responses, responses_stat[responses][0]), 'UTF-8')
        self._backlog += bytearray("Content-Type: {0}\r\n\r\n".format(content_type[target[-3:]]), 'UTF-8')
        if not rb:
            self._backlog += bytearray(data, 'utf-8')
        elif rb:
            self._backlog += bytearray(data)
        
    def _read_ready(self):
        """
        Since sockets only allow for reading a specified amount
        of bytes we can set the socket to not block on empty
        recv and continue receiving until the call fails. There
        by receiving more than the specified amount.
        """
        data = b''
        self._socket.setblocking(False)
        while True:
            try:
                r = self._socket.recv(100)
                data += r
            except (socket.timeout, socket.error):
                break
        self._socket.setblocking(True)
        if not r:
            self.done = True
            return
        print('-'+'GET REQUEST'+'-'*40)
        self.read(data)
 
    def _write_ready(self):
        """
        We only write things to the socket when it signals that
        it's ready to receive something. Not doing this an
        relying on implicit buffers works most of the time but
        this really isn't a difficult thing to implement.
        """
        if self._backlog:
            count = self._socket.send(self._backlog)
            self._backlog = self._backlog[count:]
 
 
def main_loop():
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    sock.listen(1)  # listen(1) means that we only allow new
                    # connections when the previous ones have
                    # been properly processed.
    print('Start Listening at 0.0.0.0:{0}'.format(port))
    clients = {}  # Keep a dictionary mapping sockets to clients
    try:
        while True:
            # We add `sock` to the `rlist` since it will signal
            # that it's ready to be read when a new connection is
            # waiting to be accepted.
            rlist = [sock] + list(clients.keys())
            wlist = [s for (s, c) in clients.items() if c._backlog]
            (rs, ws, _) = select.select(rlist, wlist, [])
            if ws:
                print('-'+'SENDING'+'-'*40)
            try:
                for r in rs:
                    if r == sock:
                        (s, addr) = sock.accept()
                        clients[s] = Client(addr, s)
                    elif r in clients:
                        clients[r]._read_ready()
                for w in ws:
                    if w in clients:
                        clients[w]._write_ready()
            except Exception:
                # Including this catch as an example. It's often
                # nice to handle this and then break from the loop.
                raise
            # Iterate over all the clients to find out which ones
            # the client has disconnected from so we can remove
            # their references and let them be collected.
            for s in list(clients.keys())[:]:
                if clients[s].done:
                    del clients[s]
            sock.listen(1)
    except KeyboardInterrupt:
        print("Got CTRL-C, quitting")
    finally:
        sock.close()
        
        
if __name__ == '__main__':
    main_loop()
