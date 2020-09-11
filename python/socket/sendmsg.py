import socket
#udp 只管发
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.0.102",9000))
s.sendto('send:Hello!'.encode('utf8'),("192.168.0.102",9090))
data,addr= s.recvfrom(1024)
print("地址：{}  端口号：{}  在给我发消息，消息是{}".format(addr[0],addr[1],data.decode('utf8')))
s.close()