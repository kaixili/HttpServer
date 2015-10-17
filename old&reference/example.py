import socket
import select
 
 
class Client(object):
    def __init__(self, addr, sock):
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
        for s in ss.strip().split('\n'):
            if s == "hello":
                self.write("Hello, World!\n")
 
    def write(self, data):
        self._backlog += bytearray(data, 'utf-8')
 
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
    sock.bind(("", 8002))
    sock.listen(1)  # listen(1) means that we only allow new
                    # connections when the previous ones have
                    # been properly processed.
    clients = {}  # Keep a dictionary mapping sockets to clients
    try:
        while True:
            # We add `sock` to the `rlist` since it will signal
            # that it's ready to be read when a new connection is
            # waiting to be accepted.
            rlist = [sock] + list(clients.keys())
            wlist = [s for (s, c) in clients.items() if c._backlog]
            (rs, ws, _) = select.select(rlist, wlist, [])
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
        
        
main_loop()