import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.0.102',9090))
s.sendto("recv: HI".encode("utf8"),("192.168.0.102",9000))
data,addr = s.recvfrom(1024)
print('从{}地址{}端口号接收到了消息，内容是：{}'.format(addr[0],addr[1],data.decode('utf8')))
s.close()