# 导入socket库:
import socket, threading

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999))
#监听端口
s.listen(5)
print('Waiting for connection...')
#建立永久循环来接收客户端请求
while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()