from wsgiref.simple_server import make_server
#webbrower.open('http://localhost:8000/xyz?abc')
def load_html(file_name):
    try:
        with open('/root/wsgi/'+file_name,'r',encoding='utf8')  as file:
            content=file.read()
        return content
    except FileNotFoundError:
        print("文件不存在！")
def hello():
    response_body=load_html('page.html')       
def login():
    return "欢迎来到登录页面！"
def admin():
    return  "欢迎来到管理页面！"
def register():
    return "欢迎来到注册页面！"
def noexit(self):
    self.response="404 Not Found"
    return "页面不存在！"

url = {
    '/':index,
    '/login':hello
    '/admin':admin
    '/register':register
}
def demo_app(environ,start_response):
    path= environ['PATH_INFO']
    print("path={}".format(path))
    response="200 OK"
    method = url.get(path)
    if method:   
        response_body = method()   
    else:
        response_body =noexit()
    start_response(response,[("Content-Type","text/html;charset=utf8"),("ww","sss")])
    return [response_body.encode('utf8')]

if __name__ == "__main__":
    httpd = make_server('',9092,demo_app)
    sa= httpd.socket.getsockname()
    print("serving HTTP on",sa[0],"port",sa[1])
    httpd.serve_forever()