import optparse
import os
import socket
import time
import ssl
from threading import Thread
from io import StringIO
from send_https import https_server

location = os.getcwd() + '/html'
from data2 import content_type, responses_stat


def main_https():
    _ssl = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    try:
        _ssl.load_cert_chain(certfile='cacert.pem', keyfile='privkey.pem')
    except:
        print('''ssl error!
            try: openssl req -new -x509 -days 365 -nodes -out cacert.pem -keyout privkey.pem''')
        return -1
    ss = socket.socket()
    ss.bind(('', 443))
    ss.listen(1023)
    print("HTTP server at {0}:{1}".format('0.0.0.0', 443))
    
    while True:
        try:
            client, address = ss.accept()
        except KeyboardInterrupt:
            ss.close()
            return -1
        https_server(_ssl, client, address)
        #thread = Thread(target = https_server, args = [_ssl, client, address])
        #thread.setDaemon()
        #thread.start()

main_https()