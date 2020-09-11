import socket,os
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(("192.168.0.102",9090))  
server_socket.listen(128)
client_socket,client_addr = server_socket.accept() 
filename = client_socket.recv(1024).decode("utf8")  
if os.path.isfile(filename):
    with open(filename,'rb') as file:
        content=file.read()
        client_socket.send(content)
else:
    print("文件不存在")