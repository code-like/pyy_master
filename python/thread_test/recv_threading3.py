import socket,threading
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.0.102",9090))
def sendmsg():
    while True:
        content = input("输入发送的消息（接收端）：")
        s.sendto(content.encode("utf8"),("192.168.0.102",9095))
        if content == "exit":
            break
def recvmsg():
    while True:
        data,socket_addr= s.recvfrom(1024)
        print("\n地址：{}  端口号：{}  发来消息，消息是：{}".format(socket_addr[0],socket_addr[1],data.decode('utf8')))
        if data.decode("utf8") == "exit":
            break
a = threading.Thread(target=sendmsg)
b = threading.Thread(target=recvmsg)
a.start()
b.start()

