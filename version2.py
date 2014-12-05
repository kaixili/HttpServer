import socket
from data2 import content_type, responses_stat  # 2个字典数据

def send_bytes(responses, data):
    client.send(bytes('HTTP/1.1 {0} {1}\r\n'.format(responses, responses_stat[responses][0]), 'UTF-8'))
    client.send(bytes("Content-Type: {0}\r\n\r\n".format(content_type[target[-3:]]), 'UTF-8'))
    client.send(bytes(data, 'UTF-8'))

host = ''
port = 80
backlog = 1023
size_max = 1024

location = '/home/lkx810/b'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #创建socket对象，并说明使用的是IPv4(AF_INET，IP version 4)和TCP协议(SOCK_STREAM)。
s.bind((host,port))   #绑定端口
s.listen(backlog)  

while 1:
    try:
        client, address = s.accept()
    except KeyboardInterrupt:
        s.close()

    data = client.recv(size_max) 
    print('{0} From {1}'.format(data.decode('utf-8'), address)) 
    
    
    if not data:
        continue
    data_request_address = data.decode('utf-8').split()[1]
    if data_request_address[-1] == '/':
        data_request_address += 'index.html' 
    elif data_request_address[0] != '/':
        send_bytes(411, '')   #没有地址字段 返回411 不支持空字段
    
    data_request_method = data.decode('utf-8').split()[0]
    #post 请求 留做后面处理
    #分两种情况：application/x-www-form-urlencoded 和 multipart/form-data
    #RFC 2616 以后再看
    if data_request_method == 'POST':
        print('\t POST_DATA:' + data.decode('utf-8').split()[-1])
    
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
    print()