import socket,os
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.0.102",9090))
filename = input("请输入要下载的文件名：")
s.send(filename.encode("utf8"))
with open(filename,"wb") as file:
    while True:
        content = s.recv(1024)
        if not  content:
            break
        file.write(content)

s.close()
