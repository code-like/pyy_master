import socket
class Myserver(self,ip,port):
    self.s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.s.bind((ip,port))
    self.s.listen(128)
    def run_forever():
        while True:
            client_socket,addr =self. s.accept()
            data = client_socket.recv(1024).decode('utf8')
            print(data)
            path = ''
            if data:
                path=data.splitlines()[0].split(' ')[1]
                print("path是{}".format(path))
            if path=="/":
                response_body = "欢迎来到首页！"
            elif path=="/login":
                response_body = "欢迎来到登录页面！"
            elif path=="/admin":
                response_body = "欢迎来到管理页面！"
            elif path=="/register":
                response_body = "欢迎来到注册页面！"
            else:
                response_body = "页面不存在！"
            response_header =  "HTTP/1.1 200 OK\n"+"Connection: keep-alive\n"+"\n"
            response_msg = (response_header+response_body).encode("gbk")
            
            client_socket.send(response_msg)

myserver =  Myserver("127.0.0.1",9090)
myserver.run_forever()



















