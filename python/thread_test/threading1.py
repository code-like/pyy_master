import threading,time
def dance():
    for i in range(10):
        time.sleep(0.2)
        print("正在跳舞")
def sing():
    for i in range(10):
        time.sleep(0.2)
        print("正在唱歌")  

a = threading.Thread(target=dance)    
b = threading.Thread(target=sing)    
a.start()
b.start()